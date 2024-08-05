from django.shortcuts import render
import numpy as np
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

GOOGLE_APY_KEY = str(os.getenv('GOOGLE_APY_KEY'))
genai.configure(api_key=GOOGLE_APY_KEY)


def index(request):
    return render(request, 'report/index.html')