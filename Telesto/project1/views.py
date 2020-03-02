from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .import forms
# Create your views here.


@login_required
def dashboard(request):
   
   return render(request,
                  'project1/dashboard.html',
                  {'section': 'dashboard'})


def uploadswigyfile(request):
	if request.method=="POST":
		form = forms.upload(request.POST)
		if form.is_valid():
			performance_pca=form.cleaned_data['set_of_choices']
			print(performance_pca)
			form.save(commit=True)
			form={'learning_rate':learning_rate, 
					'epochi':epochi,'standard_devaition':standard_devaition,'som_map_column':som_map_column,
					'set_of_choices':set_of_choices,'som_map_rows':som_map_rows,'set_of_choices':set_of_choices,
					performance_pca:performance_pca}

			return render(request,'project1/uploadswigyfiles.html', {'form': form})
	# Above all we write the machine learning code
	else:
		form = forms.som()
		return render(request,'project1/uploadswigyfiles.html', {'form': form})
	
    

def som(request):
	if request.method=="POST":
		form = forms.som(request.POST)
		if form.is_valid():
			learning_rate=form.cleaned_data['Learning_rate']
			epochi=form.cleaned_data['Epochi']
			standard_devaition=form.cleaned_data['standard_Deviation']
			som_map_rows=form.cleaned_data['Som_map_rows']
			som_map_column=form.cleaned_data['Som_map_column']
			set_of_choices=form.cleaned_data['set_of_choices']
			performance_pca=form.cleaned_data['set_of_choices']
			print(performance_pca)
			form.save(commit=True)
			form={'learning_rate':learning_rate, 
					'epochi':epochi,'standard_devaition':standard_devaition,'som_map_column':som_map_column,
					'set_of_choices':set_of_choices,'som_map_rows':som_map_rows,'set_of_choices':set_of_choices,
					performance_pca:performance_pca}

			return render(request,'project1/som1.html', {'form': form})
	# Above all we write the machine learning code
	else:
		form = forms.som()
		return render(request,'project1/som.html', {'form': form})
	


def clustering(request):
	if request.method=="POST":
		form = forms.clustering(request.POST)
		if form.is_valid():
			number_of_chusks=form.cleaned_data['number_of_chusks']
			max_iteration=form.cleaned_data['max_iteration']
			initailizers=form.cleaned_data['intializer']
			n_init=form.cleaned_data['n_init']
			algorithm=form.cleaned_data['algorithm']
			tolerance=form.cleaned_data['Tolerance']
			form.save(commit=True)
			form={'number_of_chusks':number_of_chusks,'max_iteration':max_iteration,'initailizers':initailizers,'n_init':n_init,
					'algorithm':algorithm,'tolerance':tolerance}
			return render(request,'project1/clustering1.html', {'form': form})
	# Above all we write the machine learning code
	else:
		form = forms.clustering()
		return render(request,'project1/clustering.html', {'form': form})
	
	
@login_required
def plots(request):
	
	return render(request,'project1/index1.html',
                  {'swigy': swigy})