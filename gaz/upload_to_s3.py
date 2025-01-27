import boto3
import argparse
from botocore.exceptions import NoCredentialsError


def upload_to_yandex_bucket(file_path, bucket_name, object_name=None):
    """
    Функция для загрузки файла в Yandex Object Storage.
    """

    print(f"Uploading {file_path} to bucket {bucket_name} as {object_name}")

    # Указываем настройки для доступа к Yandex Object Storage
    s3 = boto3.client(
        's3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id='YCAJElR67D3eYVd7M2_VA2Mja',
        aws_secret_access_key='YCPqXQNLhhWACxifyJWSG5RO9EOkhbyX59XVmckJ',
    )

    # Если имя объекта не указано, берем имя файла
    if object_name is None:
        object_name = file_path.split('/')[-1]

    # Загружаем файл в bucket
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f'{file_path} загружен как {object_name} в bucket {bucket_name}')
    except FileNotFoundError:
        print('Файл не найден.')
    except NoCredentialsError:
        print('Ошибка доступа. Проверьте ваши ключи.')


if __name__ == "__main__":
    # Создаём парсер аргументов
    parser = argparse.ArgumentParser(description="Upload a file to a Yandex Object Storage bucket.")
    parser.add_argument("bucket_name", help="Name of the Yandex bucket.")
    parser.add_argument("file_path", help="Path to the local file to upload.")
    parser.add_argument("object_name", help="Name of the object in the bucket.")

    # Парсим аргументы
    args = parser.parse_args()

    # Передаём аргументы в функцию
    upload_to_yandex_bucket(args.bucket_name, args.file_path, args.object_name)
