from flask import current_app

from sqlalchemy import text

from app.functions import (
    convert_image_to_base64,
    save_and_compress_image,
    save_file_video,
)


from ..models import News, ImageNews, VideoNews
from ..db.db import db


def add_news(title, text, bajada, category, fechaHora, author_id, files, url):
    upload_folder = current_app.config["UPLOAD_FOLDER"]

    news_data = {
        "title": title,
        "text": text,
        "bajada": bajada,
        "author_id": author_id,
        "category": category,
        "url": url,
        "fecha_hora_baja": fechaHora,
    }

    # Guardar news_data en la base de datos
    new = News(**news_data)
    db.session.add(new)
    db.session.commit()

    id_news = new.id
    is_first_image = True

    for key in files:
        if "image" in key:
            file = files[key]
            image_path = save_and_compress_image(file, upload_folder)
            if image_path:
                display_value = "primario" if is_first_image else "secundario"
                img_n = {
                    "news_id": id_news,
                    "path": image_path,
                    "priority": display_value,
                }
                img_ne = ImageNews(**img_n)
                db.session.add(img_ne)
                db.session.commit()
                # Una vez guardada la primera imagen, cambiamos el estado
                is_first_image = False

    video_file = files.get("videoFile")
    if video_file:
        video_path = save_file_video(video_file, upload_folder) if video_file else None
        video_n = {"news_id": id_news, "path": video_path}
        video_new = VideoNews(**video_n)
        db.session.add(video_new)
        db.session.commit()

    return id_news


def get_one_new(news_id):
    procedure_call = text("CALL GetNewsDetails(:news_id)")
    result = db.session.execute(procedure_call, {"news_id": news_id}).mappings().all()

    if not result:
        return None

    first_row = result[0]
    news_data = {
        "id": first_row["news_id"],
        "title": first_row["title"],
        "text": first_row["text"],
        "bajada": first_row["bajada"],
        "category": first_row["category"],
        "fecha_hora_baja": first_row["fecha_hora_baja"],
        "url": first_row["url"],
        "created_at": first_row["created_at"],
        "updated_at": first_row["updated_at"],
        "author": {
            "username": first_row["author_username"],
            "email": first_row["author_email"],
        },
        "images": [],
        "video": None,
    }

    for row in result:
        if row["image_id"]:
            image_base64 = convert_image_to_base64(row["image_path"])
            news_data["images"].append(
                {
                    "id": row["image_id"],
                    "priority": row["image_priority"],
                    "base64": image_base64,
                }
            )
        if row["video_id"]:
            news_data["video"] = {"id": row["video_id"], "path": row["video_path"]}

    return news_data


def get_all_news():
    procedure_call = text("CALL GetNews")
    result = db.session.execute(procedure_call).mappings().all()

    news_all = []
    for row in result:
        image_path = row["image_path"]
        image_base64 = convert_image_to_base64(image_path) if image_path else None

        new_data = {
            "id": row["news_id"],
            "title": row["title"],
            "category": row["category"],
            "image": image_base64,
        }
        news_all.append(new_data)

    return news_all
