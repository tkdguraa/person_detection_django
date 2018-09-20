# Person Detection Django
Person detect and alert django web application

## Requirements
`Python3, tensorflow1.0, numpy, opencv3`

## Getting started
1. Install [darkflow](https://github.com/thtrieu/darkflow) (YOLO tensorflow ver)
2. Replace `darkflow/net/yolo/process.py` and `darkflow/net/help.py` with `scripts/process.py` and `scripts/help.py`
3. Download tiny-yolo-v1.1.weights from [here](https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU), place it in `/bin` folder
4. `python manage.py migrate detection`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`
