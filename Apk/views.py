

from http.client import REQUEST_URI_TOO_LONG
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from pandas import cut
from Apk.forms import ReviewForm, SignInform, SignUpForm, TableForm, UserInfo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import razorpay

from Apk.models import Customer, Hotels, Order, Product, Reviews, Table
from onlinefood.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

# Create your views here.


def index(request,zpcode = None):

    if zpcode is not None:
         
        cust = Customer.objects.get(user = request.user)
        zpcode = cust.zipcode
        hotels = Hotels.objects.filter(zipcode = zpcode)
        
        if hotels.exists() is False:

            messages.success(request,'No Hotel Found In Your Area !!')
        
        
    else:
        hotels = Hotels.objects.all()
    
    return render(request,'base.html',{'obj':hotels})


def breakfast(request,name = None):
    
    product = Product.objects.filter(hotel_name__name =  name).filter(category__name = 'breakfast')
 
    return render(request,'breakfast.html',{'product':product})



def dinner(request,name = None):
    product = Product.objects.filter(hotel_name__name = name).filter(category__name = 'dinner')
    return render(request,'dinner.html',{'product':product})


def lunch(request, name= None):
    product = Product.objects.filter(hotel_name__name = name).filter(category__name = 'lunch')
    return render(request,'lunch.html',{'product':product})


def dessert(request,name = None):
    product = Product.objects.filter(hotel_name__name = name).filter(category__name = 'dessert')
    return render(request,'dessert.html',{'product':product})

def productdetail(request,data = None):
    product = Product.objects.filter(id = data)
    print(product)
    
    dic = {
        'product': product
    }
    return render(request, 'productdetails.html',dic)

@login_required(login_url="signin")
def payment(request,data = None):
    

        client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

        
        order_currency = 'INR'
            # OPTIONAL

        
        # getting quantity from quant input in productdetail page
        quantity = request.GET.get('quant')
        print(quantity)
        # quantity = 2

        
        fm = Customer.objects.filter(user = request.user)
        form = Product.objects.get(id = data)
        product_name = form.name
        discounted_price = form.discounted_price
        quantity = int(quantity)
        print('girish')
        discounted_price = discounted_price * quantity
        
        total = discounted_price  + 30
        order_amount = total
        print(order_amount)
        payement = client.order.create(dict(amount=order_amount, currency=order_currency,payment_capture = 1))
        payment_id = payement['id']

        
        return render(request,'payment.html',{'fm':fm,'form':form,'quant':quantity,'total':total,'api_key':RAZORPAY_API_KEY,'api_secret_key':RAZORPAY_API_SECRET_KEY,'payment_order_id':payment_id,'product_name':product_name})
    # except Exception as e:
    #     print(e)
    #     return redirect('/offline/')
def order(request,id = None, qun = None):
    
    
    
    if request.method == 'POST':
        form = Product.objects.get(id = id)
        product_name = form.name
        category = form.category
        discounted_price = form.discounted_price
        product_img = form.product_image
        print(product_img)
        quantity = int(qun)
        
        discounted_price = discounted_price * quantity
        
        total = discounted_price  + 30

        obj = Order(user = request.user, name = product_name, category = category, quantity = quantity , price = total,product_img = product_img)
        obj.save()
        return redirect('/order/')
    

    order = Order.objects.all()

    return render(request, 'order.html',{'order': order})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            print('helloe')
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your Account Has Been Created !!!")
            
            fm = SignUpForm()
            return HttpResponseRedirect('/signin/')
    else:   
        
        form = SignUpForm()
        
    return render(request,'signup.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        form = SignInform(request= request, data= request.POST)
        print('post request')
        if form.is_valid():
            print('valide')
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            print(uname)
            print(upass)

            user_obj = authenticate(request, username = uname, password = upass)

            if user_obj is not None:
                login(request,user_obj)

                return redirect('/profile/')
        
        
    else:
        form = SignInform()

    return render(request,'signin.html',{'form':form})

@login_required(login_url="signin")
def signout(request):

    logout(request)

    return redirect('/')

    
@login_required(login_url="signin")
def profile(request):

    if request.method == "POST":
        form = UserInfo(request.POST)

        if form.is_valid():
            user = request.user

            name = form.cleaned_data['Name']
            mobile = form.cleaned_data['Mobile']
            address = form.cleaned_data['Address']
            city = form.cleaned_data['City']
            district = form.cleaned_data['District']
            state = form.cleaned_data['State']
            gender = form.cleaned_data['Gender']
            zipcode = form.cleaned_data['Zipcode']

            
            
            bool_var = Customer.objects.filter(user = request.user).exists()
            mob_unique = Customer.objects.filter(mobile = mobile).exists()

            if mob_unique == True:
               
                
                pass
           
            if bool_var == False:
                
                obj = Customer(user = user,full_name = name, mobile = mobile, address = address,city = city, district = district, state = state,gender = gender, zipcode = zipcode)
                obj.save()
            else:

                # Customer.objects.update(user = user,full_name = name, mobile = mobile, address = address, state = state,gender = gender, zipcode = zipcode)
                Customer.objects.filter(user = request.user).update(user = user,full_name = name, mobile = mobile, address = address,city = city, district = district, state = state,gender = gender, zipcode = zipcode)

    else:
        form = UserInfo()
    fm = Customer.objects.filter(user = request.user)
    tbl = Table.objects.filter(user = request.user)
    tbl_bool_val = tbl.exists()
    if tbl_bool_val is False:
        messages.warning(request,'NO Table Reserved Yet !!!')
    
    return render(request, 'profile.html',{'form':form,'fm':fm,'tables':tbl})

def offline(request):
    return render(request,'offline_redirect.html')

def hotels(request,name = None):
# 
    hotel_name = request.POST.get('hotel_name')
    
    hotels = Hotels.objects.filter(name = name)
    feedbk = Reviews.objects.filter(hotel_name = name)
    if request.method == 'POST':
        
        
        rfm = ReviewForm(request.POST)

        if 'tableform' in request.POST:
            fm = TableForm(request.POST)
            if fm.is_valid():
                name = fm.cleaned_data['name']
                persons = fm.cleaned_data['persons']
                tables = fm.cleaned_data['tables']
                date = fm.cleaned_data['date']
                time = fm.cleaned_data['time']
                mobile = fm.cleaned_data['mobile']
                user = request.user

                table = Hotels.objects.filter(name = hotel_name).values('table')
                table = table[0]
                table_val = table['table']
                print(table_val)
                if table_val == 0 or table_val < tables :
                    print('run')
                    if table_val == 0:

                        messages.success(request,'All tables are booked')
                    else:
                        messages.warning(request,' Sorry !! We have not enough tables')
                else:    
                    # update the table value after booking the tables
                    print('else')
                    table_val = table_val - tables
                    Hotels.objects.filter(name = hotel_name).update(table = table_val)
                    
                    obj = Table(user = user,name = name,persons = persons,tables = tables, date = date, time= time,mobile = mobile, hotel_name = hotel_name )
                    obj.save()
                    print('book')
                    # return redirect("/profile/")

        if 'reivewform' in request.POST:

            if rfm.is_valid():
                mes = rfm.cleaned_data['message']
            
                print(name)
                robj = Reviews(hotel_name = name,user = request.user,message = mes)
                robj.save()
                print('saved')

                fm = TableForm()
    else:
        fm = TableForm()
        rfm = ReviewForm()
    
    
    return render(request,'hotels.html',{'obj':hotels,'form':fm,'rform':rfm,'feedbacks': feedbk})

def sami(request):
    return render(request,'sami.html')