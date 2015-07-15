function initJournal() {		
	$(document).on("click", '.day-box input[type="checkbox"]', function(event) {
		var indicator = $('#ajax-progress-indicator'); 
		var box = $(this);
		$.ajax(box.data('url'), {
			'type': 'POST',
			'async': true,
			'dataType': 'json',
			'data': {
				'pk': box.data('student-id'),
				'date': box.data('date'),
				'present': box.is(':checked') ? '1': '',
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
			},
			'beforeSend': function(xhr, settings){
				indicator.show();				
			},
			'error': function(xhr, status, error){
				alert(error);
				indicator.hide();
			},
			'success': function(data, status, xhr){
				indicator.hide();
			}
		});
	});
}

function initGroupSelector() {
	// look up select element with groups and our even handler
	// on field "change" event
	$('#group-selector select').change(function(event) {
		//get value of currently selected group option
		var group = $(this).val();
		
		if(group) {
			//set cookie with expiration date 1 years since now;
			// cookie creation function takes period in days
			$.cookie('current_group', group, {'path': '/', 'expires': 365});
		} else {
			// otherwise we delete the cookie
		$.removeCookie('current_group', {'path': '/'});	
		}
		
		//and reload a pageX
		location.reload(true);
		
		return true;
	});
}

function initDateFields() {	
	$('input.dateinput').datetimepicker({		
		'format': 'YYYY-MM-DD'
	}).on('dp.hide', function(event){
		$(this).blur();	
	});
}

function initEditStudentPage() {
	$(document).on("click", 'a.student-edit-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initEditStudentForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initEditStudentForm(form, modal) {
	// attach datepicker
	initDateFields();

	// close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;	
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initEditStudentForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}

function initAddStudentPage() {
	$(document).on("click", 'a#student-add-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initAddStudentForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initAddStudentForm(form, modal) {
	// attach datepicker
	initDateFields();

	// close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;	
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initAddStudentForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}

function initDeleteStudentPage() {
	$(document).on("click", 'a.student-delete-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initDeleteStudentForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initDeleteStudentForm(form, modal) {
	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initDeleteStudentForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}


function initAddGroupPage() {
	$(document).on("click", 'a#group-add-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initAddGroupForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initAddGroupForm(form, modal) {
	// close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;	
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
			modal.find('.modal-body').html('<div class="alert alert-danger" role="alert">Йде відправка даних.</div>');
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initAddGroupForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}

function initEditGroupPage() {
	$(document).on("click", 'a.group-edit-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initEditGroupForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initEditGroupForm(form, modal) {	
	// close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;	
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initEditGroupForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}

function initDeleteGroupPage() {
	$(document).on("click", 'a.group-delete-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initDeleteGroupForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initDeleteGroupForm(form, modal) {
	// close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;	
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initDeleteGroupForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}

function initAddExamPage() {
	$(document).on("click", 'a#exam-add-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initAddExamForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initAddExamForm(form, modal) {
	// attach Datepicker
	initDateFields();
	
	// close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;	
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initAddExamForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}

function initEditExamPage() {
	$(document).on("click", 'a.exam-edit-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initEditExamForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initEditExamForm(form, modal) {
	// attach Datepicker
	initDateFields();
	
	// close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;	
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initEditExamForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}

function initDeleteExamPage() {
	$(document).on("click", 'a.exam-delete-form-link', function(){
		var link = $(this);
		$.ajax({			
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',			
			'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}

				// update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form
				initDeleteExamForm(form, modal);

				// setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
				'error': function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false
			}
		});
    return false;
  });
}

function initDeleteExamForm(form, modal) {
	// attach Datepicker
	initDateFields();
	
	// close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;	
	});

	// make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
		var html = $(data), newform = html.find('#content-column form');

		// copy alert to modal window
		modal.find('.modal-body').html(html.find('.alert'));

		// copy form to modal if we found it in server response
		if (newform.length > 0) {
			modal.find('.modal-body').append(newform);
						
			// initialize form fields and buttons
			initDeleteExamForm(newform, modal);
		} else {
			// if no form, it means success and we need to reload page
			// to get updated students list;
			// reload after 2 seconds, so that user can read success message			
			setTimeout(function(){location.reload(true);}, 1800);
			}
		},
		'beforeSend': function(data, status, xhr) {
			var input = $('input', 'textarea').attr('readonly','true');	
		}
	});
}

function updatePageContext() {	
	var url = window.location.href;  
	$.ajax({
		'url': url,
		'dataType': 'html',
		'type': 'get',
		'success': function(data, status, xhr){
			
			// check if we got successfull response from the server
			if (status != 'success') {
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}
			
			// update modal window with arrived content from the server
			var table = $('.table'), newpage = $(data), newtable = newpage.find('.table');
			table.html(newtable);			
		},

		'error': function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
			return false;
		}
	});
	return false;
}


function ajaxFunctional(url) {
        $.ajax({
            'url': url,
            'dataType': 'html',
            'type': 'get',
            'success': function(newdata, status, xhr){
				
                // check if we got successfull response from the server    
                if (status != 'success') {
                    alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
                    return false;
                }
                var html = $(newdata), page = $(html.find("#content-column")), body = $('#content-column');
                body.html(page);
				var activeBar = $('.nav-tabs');
				activeBar.find('li').removeClass('active');
				var realActiveBar = $(newdata).find('.nav-tabs').find('.active');
				for (var i = 0; i<5; i++) {
					some = activeBar.find('li:eq('+i+')');
					if (some.text()==realActiveBar.text()) {
						some.addClass('active');
					}
				}

				if (!url.contains("localhost"))
				{
					history.pushState(null, document.title, url);
				}


				window.onpopstate = function() {
			  		var modal = $('#myModal');
			  		modal.modal('hide');

			  		var url2 = window.location.href; 
			  		ajaxFunctional(url2);
				};
            },

            'error': function(){
                alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
                return false;
            }
      });	
}

function UpdateAllPage() {
	$(document).on("click", "a.content-pagination, a.content-sorting, a.content-url", function() {
        var link = $(this);
        ajaxFunctional(link.attr('href'));
        return false;
    });
}

 
$(document).ready(function() {
	initJournal();
	initGroupSelector();
	initDateFields();
	initEditStudentPage();
	initAddStudentPage();
	initDeleteStudentPage();
	initAddGroupPage();
	initEditGroupPage();
	initDeleteGroupPage();
	initAddExamPage();
	initEditExamPage();
	initDeleteExamPage();
	UpdateAllPage();
});