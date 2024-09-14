# Coconut service
сервис, который прогнозирует действия <br>
пользователей интернет магазина

## Требования
- Python 3
## Запуск
### 1. Dockerfile
```shell
  docker build -t coconut_image . ; docker run --name coconut -p 8000:8000 coconut_image
```
### 2. Powershell script
```shell
    .\setup-and-run.ps1
```

## Swagger
 - http://localhost:8000/docs
