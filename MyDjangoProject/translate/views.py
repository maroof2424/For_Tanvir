from django.shortcuts import render
from googletrans import Translator

def translate_view(request):
    translator = Translator()
    text = request.GET.get('text', '')  # Get text input
    target_language = request.GET.get('lang', 'en')  # Get language

    translated_text = translator.translate(text, dest=target_language).text if text else ''

    return render(request, 'translate/translate.html', {'translated_text': translated_text})
