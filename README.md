# دادمان | چت‌بات حقوقی فارسی

نسخه آغازین قابل اجرا از چت‌بات دادمان؛ رابط فارسی راست‌چین، API با FastAPI و آداپتور مستقل برای اتصال به هر سرویس سازگار با OpenAI Chat Completions.

## پیش‌نیاز
- Python 3.10+

## اجرا
```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```
سپس `http://127.0.0.1:8000` را باز کنید.

## اتصال مدل واقعی
در فایل `backend/.env` مقدارهای زیر را تنظیم کنید:
- `LLM_BASE_URL`: آدرس پایه API سازگار با OpenAI
- `LLM_API_KEY`: کلید API
- `LLM_MODEL`: نام مدل
- `DEMO_MODE=false`

اگر تنظیمات مدل انجام نشده باشد، برنامه در حالت نمایشی پاسخ می‌دهد و ادعا نمی‌کند که پاسخ از مدل واقعی آمده است.

## مسیرهای API
- `GET /api/health`
- `POST /api/chat` با بدنه `{"messages":[{"role":"user","content":"..."}]}`

## نکته حقوقی
این نسخه صرفاً زیرساخت فنی اولیه است. بانک قوانین، آرای وحدت رویه، استناد دقیق به منابع، تاریخ اعتبار مقررات و هشدارهای حقوقی باید در مراحل بعدی اضافه و با منابع رسمی اعتبارسنجی شوند.
