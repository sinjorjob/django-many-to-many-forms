from django.shortcuts import render
from django.views.generic import CreateView
from .models import Agenda, Member
from .forms import CreateAgendaForm
from django.urls import reverse_lazy
from django.core.mail import send_mail  #追加

class SendAgenda(CreateView):
    model = Agenda
    form_class = CreateAgendaForm
    template_name = 'send_agenda.html'
    success_url = reverse_lazy('meeting:send_done')

    def form_valid(self, form):
        subject = self.request.POST.get('title')
        message = self.request.POST.get('contents')
        date = self.request.POST.get('date')
        subject = subject + "開催日：" + date
        members = self.request.POST.getlist('members')
        from_email = self.request.user.email  #送信者のアドレスを取得
        recipient_list =[]
        #送信宛アドレスを取得
        for member_pk in members:
            recipient_list.append(Member.objects.get(pk=member_pk).email)

        send_mail(subject, message, from_email, recipient_list)
        return super().form_valid(form)


def send_done(request):
    
    return render(request, 'send_done.html')