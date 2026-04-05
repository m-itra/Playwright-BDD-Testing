### 1. Создание виртуального окружения
 
```powershell
py -3.12 -m venv .venv
```
 
### 2. Активация виртуального окружения
 
```powershell
.venv\Scripts\Activate.ps1
```

### 3. Установка зависимостей
 
```powershell
pip install -r requirements.txt
```

### 4. Запуск всех тестов
 
```powershell
pytest -v
```
