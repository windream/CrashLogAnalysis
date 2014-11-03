<?
$uploaddir = './uploads/';
$uploadfile = $uploaddir. $_FILES['userfile']['name'];
print "<pre>";
if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploaddir . $_FILES['userfile']['name'])) {
    //print "File is valid, and was successfully uploaded.  Here's some more debugging info:\n";
    //print_r($_FILES);
} else {
    print "Possible file upload attack!  Here's some debugging info:\n";
    print_r($_FILES);
}
print "</pre>";
$last_line = shell_exec('./test.py '.$uploadfile);
print $last_line
?>
