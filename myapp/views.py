from django.shortcuts import render,redirect,resolve_url
from django.http import HttpResponse
from django.contrib import messages
from .models import User,UserBio,Uploads,Like,Comment,Audio_uploads
from django.urls import reverse


def index(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        users=User.objects.all()
        err=False
        for user in users:
            if(user.user_name==user_name):
                if(user.password==password):
                    # return render(request,'myapp:home',usr_id=user.id)
                    return redirect(reverse("myapp:homepage", args=(user.id,)))
                    
                else:
                    messages.info(request,"Password is incorect")
                    return redirect(reverse('myapp:index'))

            if(user_name=="" or password==""):
                
                messages.info(request,"Fill all details")
                return redirect(reverse('myapp:index'))
        else:
            messages.info(request,"No user found")
            return redirect(reverse('myapp:index'))       
    return render(request,'register.html')

def create_acnt(request):
    if request.method=="POST":
        user_name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        retype_password=request.POST['retypepassword']

        users=User.objects.all()
        err=False
        for user in users:
            if(user.user_name==user_name):
                messages.info(request,"Username is already taken")
                return redirect(reverse("myapp:create_acnt"))
        if(password!=retype_password):
            messages.info(request,"Passwords dosent match")
            return redirect(reverse("myapp:create_acnt"))
            
        if(user_name=="" or email=="" or password=="" or retype_password==""):
            messages.info(request,"Fill all the details")
            return redirect(reverse("myapp:create_acnt"))
        else:
            user=User.objects.create(user_name=user_name,email=email,password=password)
            user.save()
            user=User.objects.get(user_name=user_name)
            user_bio=UserBio.objects.create(user=user,bio_name="Bio_name",bio="Enter Your Bio",links="Links")
            user_bio.save()
            messages.info(request,"User Created sucessfully")
            return redirect(reverse("myapp:create_acnt"))
            
    return render(request,'create_acnt.html')

def homepage(request,usr_id):
    print(usr_id)
    temp=User.objects.get(id=usr_id)
    upload=Uploads.objects.all().order_by('-upload_id')
    like=Like.objects.filter(user=usr_id)
    ##
    like_list=[]
    all_audio=Audio_uploads.objects.all().order_by('-audio_id')
    for u in upload:
        a=Like.objects.filter(user=temp,upload=u).exists()
        if a:
            like_list.append(1)
        else:
            like_list.append(0)
    
    content={
        'user':temp,
        'uploads':upload,
        'zip_list':zip(upload,like_list),
        'all_audio':all_audio,
    }
    return render(request,'homepage.html',content)

def common_profile(request,usr_id):
    temp=User.objects.get(id=usr_id)
    user=User.objects.get(id=usr_id)
    temp_bio=UserBio.objects.get(user=user)
    content={
        'user':temp,
        'usr_bio':temp_bio,
    }

    return render(request,'common_profile.html',content)

def profile(request,usr_id):
    temp=User.objects.get(id=usr_id)
    user=User.objects.get(id=usr_id)
    temp_bio=UserBio.objects.get(user=user)
    content={
        'user':temp,
        'usr_bio':temp_bio,
    }
    if request.method=="POST":
        # if 'images' in request.POST:
        #     print("hello")
        #     images=request.FILES['file1']
        #     user.image=images
        #     user.save()
        #     return redirect(reverse("myapp:profile", args=(user.id,)))
            
        if('bio_name' and 'bio' and 'link' in request.POST):
            bio_name=request.POST['bioname']
            bio=request.POST['bio']
            link=request.POST['link']
            if(bio_name=="" or bio=="" or link==""):
                messages.info(request,"Fill all the details")
                return redirect(reverse("myapp:profile", args=(user.id,)))
            b=UserBio.objects.get(user=user)
            b.bio_name=bio_name
            b.bio=bio
            b.links=link
            b.save()
            messages.info(request,"Updated Sucessfully")
            return redirect(reverse("myapp:profile", args=(user.id,)))
        
        else:
            print("hai")
            image=request.FILES['file1']
            user.image=image
            user.save()
            return redirect(reverse("myapp:profile", args=(user.id,)))
        
    return render(request,'profile.html',content)



def upload_pictures(request,usr_id):

    if(request.method=='POST'):
        image=request.FILES['file1']
        content=request.POST['content']
        
        if(image=="" or content==""):
            messages.info(request,"Cannont upload")
            return redirect(reverse('myapp:upload_pictures',args=(usr_id,)))

        user=User.objects.get(id=usr_id)
        up=Uploads.objects.create(user=user,image=image,content=content)
        up.save()
        messages.info(request,"Uploaded sucessfully")
        return redirect(reverse('myapp:upload_pictures',args=(usr_id,)))
    user=User.objects.get(id=usr_id)   
    content={
        'user':user,
    } 

    return render(request,"upload_pictures.html",content)


def like(request,usr_id,post_id,us_id):
    if request.method=="POST":
        print("Hello sucess");
        user=User.objects.get(id=usr_id)
        post=Uploads.objects.get(upload_id=post_id)
        current_likes=post.likes
        liked=Like.objects.filter(user=user,upload=post).count()
        if not liked:
            Like.objects.create(user=user,upload=post)
            current_likes+=1
        else:
            Like.objects.filter(user=user,upload=post).delete()
            current_likes-=1
        post.likes=current_likes
        post.save()      
        return HttpResponse("done")


def comment(request,usr_id,post_id):
    user=User.objects.get(id=usr_id)
    upload=Uploads.objects.get(upload_id=post_id)
    comments=Comment.objects.filter(upload=upload)
    content={
        'user':user,
        'full_comments':comments,
    }
    return render(request,"comment.html",content)

def comment_upload(request,usr_id,post_id,us_id):
    if request.method=="POST":
        uploaded_comment=request.POST['comments']
        if(uploaded_comment==""):
            print("No way")
            return HttpResponse("done")
        print("Comment posted")
        user=User.objects.get(id=usr_id)
        post=Uploads.objects.get(upload_id=post_id)
        Comment.objects.create(user=user,upload=post,comments=uploaded_comment)
        
def upload_audio(request,usr_id):
    
    if(request.method=='POST'):
        audio=request.FILES['file1']
        audio_name=request.POST['audio1_name']
        
        if(audio=="" or audio_name==""):
            messages.info(request,"Cannont upload")
            return redirect(reverse('myapp:upload_audio',args=(usr_id,)))

        user=User.objects.get(id=usr_id)
        up=Audio_uploads.objects.create(user=user,audio=audio,audio_name=audio_name)
        up.save()
        messages.info(request,"Uploaded sucessfully")
        return redirect(reverse('myapp:upload_audio',args=(usr_id,)))
    user=User.objects.get(id=usr_id)   
    content={
        'user':user,
    } 

    return render(request,"upload_audio.html",content)

def audio_comment(request,usr_id,audio_id):
    pass


def audio_page(request,usr_id):
    temp=User.objects.get(id=usr_id)
    all_audio=Audio_uploads.objects.all().order_by('-audio_id')

    content={
        'user':temp,
        'all_audio':all_audio,
    }
    return render(request,'audio_play.html',content)

def myuploads(request,usr_id):
    temp=User.objects.get(id=usr_id)
    upload=Uploads.objects.filter(user=temp)
    all_audio=Audio_uploads.objects.filter(user=temp)
    content={
        'user':temp,
        'uploads':upload,
        'all_audio':all_audio,
    }
    return render(request,'myuploads.html',content)

def remove(request,post_id):
    post=Uploads.objects.get(upload_id=post_id)
    post.delete()
    usr_id=post.user.id
    return redirect(reverse('myapp:myuploads',args=(usr_id,)))

def remove_audio(request,audio_id):
    audio=Audio_uploads.objects.get(audio_id=audio_id)
    audio.delete()
    usr_id=audio.user.id
    return redirect(reverse('myapp:myuploads',args=(usr_id,)))

def purchase_premium(request,usr_id):
    premium=User.objects.get(id=usr_id)
    
    if(premium.premium==1):
        premium.premium=0
        premium.save()
    else:
        premium.premium=1
        premium.save()
    return redirect(reverse("myapp:profile", args=(usr_id,)))
    