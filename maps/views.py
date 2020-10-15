from django.shortcuts import render
import folium
# Create your views here.
def showmapwithfolium(request):
    lat_long = [35.3369, 127.7306]
    m = folium.Map(lat_long, zoom_start=10)
    popText = folium.Html('<b>Jirisan</b></br>'+str(lat_long),script=True) # lat_long이 리스트이기 때문에 str로 변환
    popup = folium.Popup(popText, max_width=2650) # max_width는 굳이 안해줘도 되지만 써야되는 상황도 생김, 2650은 해상도를 나타냄
    folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
    m = m._repr_html_() # google colabotory에서는 이 구문을 안적어도 된다.
    datas = {'mountain_map':m} # data['page_obj'] 이거랑 같은 뜻
    return render(request, 'maps/showmapwithfolium.html', context=datas)