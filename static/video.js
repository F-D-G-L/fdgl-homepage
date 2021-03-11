(function() {
	window.iframes = [];
	document.addEventListener("DOMContentLoaded", function() {
		var frame, wall, src;
		for (var i=0, max = window.frames.length - 1; i <= max; i+=1) {
			frame = document.getElementsByTagName('iframe')[0];
			src = frame.src;
			if (src.match(/youtube/) == null) {
				continue;
			}
			iframes.push(frame);
			wall = document.createElement('article');
			if (typeof (window.frames[0].stop) === 'undefined') {
				setTimeout(function() { window.frames[0].execCommand('Stop'); },1000);
			} else {
				setTimeout(function() { window.frames[0].stop(); },1000);
			}
			wall.setAttribute('class', 'video-wall');
			wall.setAttribute('data-index', i);
			wall.innerHTML = '<strong>Click f&uuml;r YouTube Video</strong><br><button class="btn"><i class="fab fa-youtube-square" aria-hidden="true"></i></button>';
			frame.parentNode.replaceChild(wall, frame);
			document.querySelectorAll('.video-wall button')[i].addEventListener('click', function() {
				var frame = this.parentNode;
				index = frame.getAttribute('data-index');

				iframes[index].src = iframes[index].src.replace(/www\.youtube\.com/, 'www.youtube-nocookie.com');
				frame.parentNode.replaceChild(iframes[index], frame);
			}, false);
		}
	});
})();
