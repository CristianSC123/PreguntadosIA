from django.shortcuts import render
from django.http import JsonResponse
import requests
'''def index(request):
    if (request.method == "GET"):
        return render(request, "index.html")'''
    
'''def index (request, nombre):
    
    return JsonResponse(data)
#Enviar un parametro 
'''

#Query
'''def index(request):
    nombre = request.GET.get("nombre")
    data = {
        "nombre": nombre,
        "mensaje": "ok",
        "ci": 13693493,
        "activo": True
    }
    return JsonResponse(data)'''
    

    
def index(request):
    prompt = None
    ACCOUNT_ID = "72fdfbfe0c10aa24a862f6cc0fceaeeb"
    AUTH_TOKEN = "3EQZOZusU8mtOATuJ8p3BdgorvfqYSNkVMNgU9OW"
    
    if(request.method == "POST"):
        prompt = request.POST.get("prompt")
        response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/google/gemma-3-12b-it",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
            "messages": [
            {"role": "system", "content": "eres un programador experto en python y django"},
            {"role": "user", "content": prompt}
            ],
            }
    )
    response_data = response.json()
    response_text = response_data.get("result", {}).get("response", "No response available")
    return render(request, "index.html", {"response": response_text})
        
