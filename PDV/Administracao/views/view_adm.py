from django.views import View
from django.shortcuts import render, redirect

class AdmView(View):

    def get(self, request):
        if not 'Usuario' in request.session:
            return redirect("loginUsuario")
        
        return render(request,'index.html')