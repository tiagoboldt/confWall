$(function(){
	$('.query').tweet({
		query: '#agilept',
		count: 7,
		avatar_size: 48,
		refresh_interval: 10,
		loading_text: 'loading tweets...'
	});

	$('.slideshow').cycle({
		fx: 'fade',
		timeout: 6000
	});

});
