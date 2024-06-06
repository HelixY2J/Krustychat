from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def chat_view(request):
    chat_grp = get_object_or_404(chatGrp, group_name="plankton_plays")
    chat_messages = chat_grp.chat_messages.all()[:30]
    form = Chatmsgform()

    if request.htmx:
        form = Chatmsgform(request.POST)

        if form.is_valid:
            msg = form.save(commit=False)
            msg.author = request.user
            msg.group = chat_grp
            msg.save()
            context = {
                'message' : msg,
                'user' : request.user
            }
            return render(request,'rt_chat/partials/chat_messages_p.html',context)

    return render(request,'rt_chat/chat.html',{'chat_messages' : chat_messages, 'form' : form})
