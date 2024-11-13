function logout_toggle() {
	const logout_btn = document.getElementById('logout-btn');
	if (logout_btn.classList.contains('hidden-element')){
		logout_btn.classList.remove('hidden-element');
	} else {
		logout_btn.classList.add('hidden-element');
	}
}

function toggleClasesContent(classCode) {
	const container_question = document.getElementById('content_clase_' + classCode);
	const arrow = document.getElementById('arrow_' + classCode);
	if (container_question.classList.contains('hidden-element')){
		container_question.classList.remove('hidden-element');
		arrow.innerHTML = '&#8744;';
	} else {
		container_question.classList.add('hidden-element');
		arrow.innerHTML = '&#62;';
	}
}

