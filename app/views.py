from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProjectForm
from .models import Product


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CreateProductView(generic.CreateView):
	model = Product
	form_class=ProjectForm
	success_url= reverse_lazy('cartlist')
	template_name='product.html'

	def form_valid(self,form):
		if self.request.user:
			form_data=form.save(commit=False)
			form_data.owner=self.request.user
			form_data.save()
			return super(CreateProductView, self).form_valid(form)
		return redirect('product')


class ProductDetailView(generic.ListView):
	model= Product
	template_name = "product_details.html"
	context_object_name = 'items'
	# queryset = Product.objects.fiter(pk=self.request.user.id)
	def get_queryset(self):
		if self.request.user.is_superuser:
			return Product.objects.all()
		return Product.objects.filter(pk=self.request.user.id)

class UpdateProductView(generic.UpdateView):
	model = Product
	form_class=ProjectForm
	template_name = 'product_edit.html'
	success_url= reverse_lazy('cartlist')

def destroy(request,pk):  
    product_id = Product.objects.get(pk=pk)  
    product_id.delete()  
    return redirect("cartlist")  