from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import room, State,District,Locations,Temporary,City,Gallerys,Reg_Mess_Restaurent
import json
from accounts.models import Profile
from django.core.mail import send_mail
from django.views.generic import View
from .mixins import HttpResponseMixin
from django.views.generic.edit import UpdateView
# from .forms import roomForm
from django.contrib import messages
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def index(request):
    state = State.objects.all()
    if request.method == 'POST' :
        state_id = request.POST.get("state")
        state = State.objects.get(id=state_id)
        dist_id = request.POST.get("district")
        dist = District.objects.get(id=dist_id)
        city_id = request.POST.get("city")
        city = City.objects.get(id = city_id)
        location_id = request.POST.get("district")
        location = Locations.objects.get(id=location_id)
        AllowedFor = request.POST.get("selectFor")
        House_type = request.POST.get("House_type")

        SearchedObject = room.objects.filter(Q(state__icontains=state.name) and  Q(AllowedFor__icontains=AllowedFor)and Q(House_type__icontains=House_type)and Q(district__icontains= dist.name) and Q(city__icontains= city.name)and Q(location__icontains= location.name))
        reco = room.objects.filter(city=city.name)
        if SearchedObject is None:
            messages.info(request, 'No Result Found As of Now')
            return redirect('/')
        return render(request,'SearchResult.html',{'SearchResult':SearchedObject,'Reco':reco})
    state = State.objects.all()
    Restaurents = Reg_Mess_Restaurent.objects.all()
    for i in Restaurents:
        print(i.city,i.phone_no,i.Mess_name,i.Mess_img)

    gallery = Gallerys.objects.all()
    Room = room.objects.all().filter(Premium = True)
    return render(request,'index11.html',{'RoomDetail':Room,'state':state,'gallery':gallery,'Resto':Restaurents})


# Create your views here.
def About(request):
    return render(request,'about.html')


def Districts(request):
    state_id = request.GET.get('state')
    # print("selected state is ",state_id)
    dist = District.objects.filter(state_id = state_id).order_by('name')
    return render(request,'load_country.html',{'dists':dist})

def city(request):
    dist_id = request.GET.get('dist')
    # print("selected district is yahi hai ",dist_id)
    dist = City.objects.filter(dist_id = dist_id).order_by('name')
    return render(request,'load_country.html',{'dists':dist})


def locations(request):
    city_id = request.GET.get('city')
    # print("selected city is yahi hai ",city_id)
    dist = Locations.objects.filter(city_id = city_id).order_by('name')
    return render(request,'load_country.html',{'dists':dist})


@login_required()
def UploadHouseDetail(request):
    state = State.objects.all()
    if request.method =='POST':
         user = request.user.profile
         Ownername = request.POST.get('Ownername')
         phone = request.POST.get('phone')
         Altphone = request.POST.get('Altphone')
         FlatAdress = request.POST.get('FlatAdress')
         landmark = request.POST.get('landmark')
         state_Id = request.POST.get('programming')
         statee = State.objects.get(id = state_Id)
         dist_Id = request.POST.get('courses')
         dist = District.objects.get(id=dist_Id)
         city_Id = request.POST.get('city')
         city = City.objects.get(id=city_Id)
         location_Id = request.POST.get('location')
         location = Locations.objects.get(id=location_Id)
         pincode = request.POST.get('pincode')
         Building_image = request.FILES.get('Building_image')
         Room_image = request.FILES.get('Roomimage')
         Owner_image = request.FILES.get('ownerimage')
         Kitchen_image = request.FILES.get('Kitchenimage')
         Bathroom_image = request.FILES.get('Bathroomimage')
         HouseDescription = request.POST.get('HouseDescription')
         AllowedFor = request.POST.get('AllowedFor')
         House_type = request.POST.get('House_type')
         Houselink = request.POST.get('Houselink')
         Housemap = request.POST.get('Housemap')
         Videofile = request.FILES.get('Video_uploads')
         Price = request.POST.get('Price')
         Housemap1 = Housemap[13:271]
         # print(Housemap1)
         # print("length of map code hai tera",len(Housemap1))


         Temporary.objects.create(user=user,Owner_Name=Ownername,Owner_pic=Owner_image,House_address=FlatAdress,Landmark=landmark,House_Location_link=Houselink,House_Location_map=Housemap1,
                                   House_type=House_type,House_description=HouseDescription,AllowedFor=AllowedFor,state = statee.name,city=city.name,
                                   district=dist.name,location=location.name,pin_no=pincode,phone_no=phone,Building_img1= Building_image,Room_img1=Room_image,
                                   Room_img2=Kitchen_image,Room_img3= Bathroom_image,House_video=Videofile,Alt_phone_no=Altphone,Price=Price).save()
         send_mail("Validate This user to upload ", "http://127.0.0.1:8000/rent/validationpage/",
                   'sachinkumar72353@gmail.com', ['sachinkumar72353@gmail.com', 'nileshkumar1009@gmail.com'])
         return redirect('/')

    context = {'state':state}
    return render(request, 'FormUpload.html', context)
 

def HouseDetail(request,pk):
    Room = room.objects.filter(id = pk)
    return render(request,'property-single.html',{'Detail':Room})




def Allmess(request):
    state = State.objects.all()
    return render(request,'All_mess.html',{'state':state})


def Single_view_mess(request,pk):
    MessDetail = Reg_Mess_Restaurent.objects.filter(id=pk)

    return render(request,'mess_single.html',{'Details':MessDetail})




@login_required()
def RegisterMess(request):
    state = State.objects.all()
    if request.method == 'POST':
        user = request.user.profile
        Ownername = request.POST.get('Ownername')
        Messname = request.POST.get('Messname')
        phone = request.POST.get('phone')
        MessAdress = request.POST.get('MessAdress')
        landmark = request.POST.get('landmark')
        state_Id = request.POST.get('programming')
        statee = State.objects.get(id=state_Id)
        dist_Id = request.POST.get('courses')
        dist = District.objects.get(id=dist_Id)
        city_Id = request.POST.get('city')
        city = City.objects.get(id=city_Id)
        location_Id = request.POST.get('location')
        location = Locations.objects.get(id=location_Id)
        pincode = request.POST.get('pincode')
        Mess_image = request.FILES.get('Mess_image')

        MessDescription = request.POST.get('MessDescription')

        Messlink = request.POST.get('Messlink')
        Messmap = request.POST.get('Messmap')


        Messmap1 = Messmap[13:271]
        # print(Housemap1)
        # print("length of map code hai tera",len(Housemap1))

        Reg_Mess_Restaurent.objects.create(user=user, Mess_Owner_name=Ownername,Mess_name=Messname, Mess_address=MessAdress,
                                 Landmark=landmark, Mess_Location_link=Messlink,  Mess_Location_map_Code=Messmap1,
                                  Mess_description=MessDescription,
                                 state=statee.name, city=city.name,
                                 district=dist.name, location=location.name, pin_no=pincode, phone_no=phone,
                                 Mess_img=Mess_image
                                 ).save()
        return redirect('/')

    context = {'state': state}
    return render(request, 'RegisterMess.html', context)


def AllProperty(request):
    Room = room.objects.all().filter(Premium=True)

    return render(request,'property-grid.html',{'rooms':Room})

def PropertyDetail(request):

    return render(request,'property-single.html')

# @method_decorator(login_required, name ="dispatch")
# class ProfileUpdateView(UpdateView):
#     model = Profile
#     fields = {'name','phone_no','Contact_Email','city','state','Profile_pic'}


@login_required()
def ValidationPage(request):
    if request.user.is_superuser:
        val = Temporary.objects.all().order_by("-id")
        return render(request,'Validate.html',{'Forvalidate':val})
    else:
        return HttpResponse('<h1>Access - Denied </h1>')

def Validate(request,pk):
    if request.user.is_superuser:

        getvalue = Temporary.objects.filter(id = pk)
        for i in getvalue:
            room.objects.create(user=i.user, Owner_Name=i.Owner_Name, House_address=i.House_address, Landmark=i.Landmark,
                                     House_Location_link=i.House_Location_link,House_Location_map=i.House_Location_map,
                                     House_type=i.House_type, House_description=i.House_description, AllowedFor=i.AllowedFor,
                                     state=i.state, city=i.city,location=i.location,Owner_pic=i.Owner_pic,
                                     district=i.district, pin_no=i.pin_no, phone_no=i.phone_no, Building_img1=i.Building_img1,
                                     Room_img1=i.Room_img1,
                                     Room_img2=i.Room_img2, Room_img3=i.Room_img3, House_video=i.House_video,
                                     Alt_phone_no=i.Alt_phone_no, Price=i.Price).save()

        Temporary.objects.filter(id=pk).delete()
    return HttpResponse("<h1>Validated </h1>")


def deletePostValidation(request,pk):
    Temporary.objects.filter(id=pk).delete()
    return HttpResponse("<h> Deleted the Post </h1>")

def mypost(request):
    # data = Mypost.objects.filter(profile=request.user.profile.id).order_by("-id")
    uploaded_by = request.user.profile.id
    # print(request.user.profile)

    context = {'data':room.objects.all().filter(user=request.user.profile).order_by("-id")}
    # # for i in data:
    # #     print(i.Article,i.Postedvideo.News_Heading)
    return render(request,'Mypost.html',context)

def DeletePost(request,pk):
    room.objects.filter(id = pk).delete()
    return render(request,'index11.html')


def EditPost(request,pk):
    Video.objects.filter(id = pk).update()
    return render(request,'Mypost.html')




# class JsonCBV(HttpResponseMixin,View):
#
#     def get(self,request,id,*args,**kwargs):
#         dataval = room.objects.get(id=id)
#         print("selected id data is here ", dataval)
#         data = {'Owner_name': dataval.Owner_Name,
#                 # 'Building_img': dataval.Building_img1,
#                 # 'Room_img1': dataval.Room_img1,
#                 'House_type': dataval.House_type,
#                 'House_address': dataval.House_address,
#                 'Price': dataval.Price}
#         json_data = json.dumps(data)
#         print("Laqad chata gya madharchod", data)
#         return self.render_to_Http_response(json_data)
#     def post(self,request,id,*args,**kwargs):
#         dataval = room.objects.get(id=id)
#         print("selected id data is here ", dataval)
#         data = {'Owner_name': dataval.Owner_Name,
#                 'Building_img': dataval.Building_img1,
#                 'Room_img1': dataval.Room_img1,
#                 'House_type': dataval.House_type,
#                 'House_address': dataval.House_address,
#                 'Price': dataval.Price}
#         json_data = json.dumps(data)
#         print("Laqad chata gya madharchod", data)
#         return self.render_to_Http_response(json_data)
#     def put(self,request,id,*args,**kwargs):
#         dataval = room.objects.get(id=id)
#         print("selected id data is here ",dataval)
#         data = {'Owner_name': dataval.Owner_Name,
#                 'Building_img': dataval.Building_img1,
#                 'Room_img1': dataval.Room_img1,
#                 'House_type': dataval.House_type,
#                 'House_address': dataval.House_address,
#                 'Price': dataval.Price}
#         json_data = json.dumps(data)
#         print("Laqad chata gya madharchod",data)
#         return self.render_to_Http_response(json_data)
#     def delete(self,request,id,*args,**kwargs):
#         dataval = room.objects.get(id=id)
#         print("selected id data is here ", dataval)
#         data = {'Owner_name': dataval.Owner_Name,
#                 # 'Building_img': dataval.Building_img1,
#                 # 'Room_img1': dataval.Room_img1,
#                 'House_type': dataval.House_type,
#                 'House_address': dataval.House_address,
#                 'Price': dataval.Price}
#         json_data = json.dumps(data)
#         print("Ld ta", data)
#         return self.render_to_Http_response(json_data)

from django.core.serializers import serialize

class JsonCBV(HttpResponseMixin,View):

    def get(self,request,id,*args,**kwargs):
        dataval = room.objects.all()
        json_data = serialize('json',dataval,fields = ('state','city','House_type','House_address','Price'))

        return self.render_to_Http_response(json_data)


def dummy(request):
    return render(request,'registerpop.html')

