var editor = ace.edit("editor");
document.getElementById('editor').style.fontSize = '14px';
editor.setTheme("ace/theme/monokai");
editor.getSession().setMode("ace/mode/xml");
editor.getSession().setUseWrapMode(true);
var data = "the new text here. "; // This should be fetched from db and copied
editor.setValue(data);

var editors = ace.edit("editors");
document.getElementById('editors').style.fontSize = '14px';
editors.setTheme("ace/theme/monokai");
editors.getSession().setUseWrapMode(true);
editors.getSession().setMode("ace/mode/xml");

function clicked(btnName, elem) {
	var selection;
	var selection_text;

	selection = editor.getSelectedText();
	selection_text = selection.toString();
	if ($(elem).hasClass("ul_tags")) {
		selection_text = "<" + btnName + ">" + "\n" + "\t" + selection + "\n" + "</" + btnName + ">";
	}
	if ($(elem).hasClass("ul_attribs")) {
		selection_text = " " + btnName + "=" + "\"\"";
	}
	editor.$blockScrolling = Infinity
	range = editor.selection.getRange();
	editor.session.replace(range, selection_text);
}

function upload_file(e) {
	var file = e.target.files[0];
	if (!file) {
		return;
	}
	var reader = new FileReader();
	reader.onload = function (e) {
		var data = e.target.result;
		display_contents(data);
	};
	reader.readAsText(file);
}

function display_contents(data) {
	var editor = ace.edit("editor");
	document.getElementById('editor').style.fontSize = '14px';
	editor.setValue(data);
}

function append_data_to_editor(elm) {
	var editors = ace.edit("editors");
	current_data = editors.getSession().getValue()
	new_data = editor.getSession().getValue()
	editors.setValue(current_data + '\n' + new_data);
}

$('li').click(function () {
	clicked($(this).text().trim(), $(this));
});

$('#uploadFile').change(function () {
	upload_file(event)
});

$('#appendData').click(function () {
	append_data_to_editor()
});

$("input[name=upload_image]").change(function () {
    if (this.files && this.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            var img = $('<img>').attr('src', e.target.result);
            $('#imageUpload').html(img);
        };
        reader.readAsDataURL(this.files[0]);
    }
});
