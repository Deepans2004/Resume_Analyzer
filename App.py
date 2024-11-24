from multiprocessing.managers import convert_to_error

import streamlit as st
import pandas as pd
import base64, random
import time,datetime

from mdurl import encode
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io,random
from streamlit_tags import st_tags
from PIL import Image
import pymysql
from Courses import ds_course,web_course,android_course,ios_course,uiux_course,resume_videos,interview_videos
import pafy
import plotly.express as px
import nltk
nltk.download('stopwords')

def fetch_yt_video(link):
    video = pafy.new(link)
    return video.title

def get_table_download_link(df,filename,text):
    csv=df.to_csv(index=False)
    b64=base64.b64encode(csv.encode()).decode()
    href=f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>
    return href

def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter=TextConverter(resource_manager,fake_file_handle,laparams=LAParams)
    page_interpreter=PDFPageInterpreter(resource_manager,converter)
    with open(file, 'rb')as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text=fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()
    return text

def show_pdf(file_path):
    with open(file_path,"rb")as f:
        base64_pdf=base64.b64encode(f.read()).decode('utf-8')
    pdf_display=F'<iframe src="data:application/pdf;base64,{base64_pdf}'width="700" h

