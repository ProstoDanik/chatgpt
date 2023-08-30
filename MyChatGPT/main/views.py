from django.shortcuts import render
import openai
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        txt = request.POST.get('txt', None)

        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=txt,
            temperature=0.5,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )

        return render(request, 'main/index.html', {'result': response['choices'][0]['text'], 'txt': txt})

    return render(request, 'main/index.html')
