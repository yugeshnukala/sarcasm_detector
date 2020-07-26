from django.shortcuts import render
from .forms import Headline

# Create your views here.
from .apps import PredictorConfig
from django.http import HttpResponse
from rest_framework.views import APIView
from nltk.corpus import stopwords

class call_model(APIView):
    def get(self, request):
        form = Headline()
        if request.method == "GET":

            form = Headline(request.GET)
            if(form.is_valid()):
                # get sentence from request
                sentence = form.cleaned_data['headline']
                # print(sentence)
                #clean the string
                sentence = sentence.split()
                string = ''
                for word in sentence:
                    if(len(word) > 2):
                        string = string +' '+ word
                sentence = string

                # vectorize sentence
                vector = PredictorConfig.vectorizer.transform([sentence])
                # predict based on vector
                prediction = PredictorConfig.regressor.predict(vector)[0]
                if(prediction == [0]):
                    return render(request,"predictor/success.html",{"result":"Not Sarcastic"})
                else:
                    return render(request,"predictor/success.html",{"result":"Sarcastic"})

def predictor(request):
    form = Headline()
    context = {
        "form": form
    }
    return render(request,'predictor/detector_html.html',context)
