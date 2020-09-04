from django.shortcuts import render
from .forms import Headline

# Create your views here.
from .apps import PredictorConfig
from django.http import HttpResponse
from django.views import View

class call_model(View):
    def get(self, request):
        form = Headline(request.GET)
        if(form.is_valid()):
            # get sentence from request
            sentence = form.cleaned_data['headline']
            # print(sentence)

            # vectorize sentence
            vector = PredictorConfig.vectorizer.transform([sentence])
            # predict based on vector
            prediction = PredictorConfig.regressor.predict(vector)[0]
            form = Headline()
            context = {
                "form":form
            }
            if(prediction == [0]):
                context['result'] = "Not Sarcastic"
            else:
                context['result'] = "Sarcastic"
            return render(request,"predictor/detector_html.html",context)

def predictor(request):
    form = Headline()
    context = {
        "form": form
    }
    return render(request,'predictor/detector_html.html',context)
