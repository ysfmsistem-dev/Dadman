import httpx
from .config import settings

async def generate_reply(messages: list[dict[str, str]]) -> tuple[str, str]:
    if settings.demo_mode or not all([settings.llm_base_url, settings.llm_api_key, settings.llm_model]):
        last = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
        return (
            "پیام شما دریافت شد. دادمان در حال حاضر در حالت نمایشی است و هنوز به مدل زبانی واقعی متصل نشده است. "
            "برای دریافت پاسخ حقوقی واقعی، مدیر سامانه باید تنظیمات اتصال مدل را در فایل .env تکمیل کند.\n\n"
            f"موضوع مطرح‌شده: {last[:500]}",
            "demo",
        )

    url = settings.llm_base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": settings.llm_model,
        "messages": [{"role": "system", "content": settings.system_prompt}, *messages],
        "temperature": 0.2,
    }
    headers = {"Authorization": f"Bearer {settings.llm_api_key}"}
    async with httpx.AsyncClient(timeout=90) as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
    return data["choices"][0]["message"]["content"], "model"
