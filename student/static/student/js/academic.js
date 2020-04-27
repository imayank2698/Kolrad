function validate(){

  //debugger;

  document.getElementById('fnameError').style.display='none';//first make the error message hidden.
  document.getElementById('lnameError').style.display='none';
  document.getElementById('emailError').style.display='none';
  document.getElementById('noError').style.display='none';
  document.getElementById('departmentError').style.display='none';
  document.getElementById('divisionError').style.display='none';
  document.getElementById('rollError').style.display='none';
  document.getElementById('cgpaError').style.display='none';



  var fname=document.getElementById('ssc').value.trim();
  var lname=document.getElementById('hsc').value.trim();//trim the extra white spaces
  var email=document.getElementById('email').value.trim();
  var pno=document.getElementById('pno').value.trim();
  var department=document.getElementById('department').value.trim();
  var division=document.getElementById('division').value.trim();
  var roll_no=document.getElementById('rno').value.trim();
  var cgpa=document.getElementById('cgpa').value.trim();


  var success=true;


  if (fname === '') {
    success=false;
    document.getElementById('fnameError').style.display='inline';//to show elements which are hidden
  }
  /*else {
    var u=/^[a-z0-9]+$/;//regular  expression object lies within / /
    if (!u.test(username)) {//if the test fails invert the result
      success=false;
      document.getElementById('usernameError2').style.display='inline';
    }
  }*/

  if (lname === '') {
    success=false;
    document.getElementById('lnameError').style.display='inline';
  }

  if (!(pno.length==10)){
        success=false;
        document.getElementById('noError').style.display='inline';
  }
  /*else {
    var pe=/^[0-9]{5}[a-z]{0,14}(\$|\*)$/;//{} no of compulsory occurences \$ was written to escape it as it is a special char in regexp
    if (!pe.test(password)) {
      success=false;
      document.getElementById('passwordError4').style.display='inline';
    }
  }*/

  var em=/^[a-z]+[0-9]*(\@)[a-z]+(\.)[a-z]+$/;
  if (!em.test(email)) {
    success=false;
    document.getElementById('emailError').style.display='inline';
  }

  if (roll_no === '') {
    success=false;
    document.getElementById('rollError').style.display='inline';
  }
  if(department ==='-1'){
    success=false;
    document.getElementById('departmentError').style.display='inline';
  }
  if(division ==='-1'){
    success=false;
    document.getElementById('divisionError').style.display='inline';
  }
  if(cgpa ==='-1'){
    success=false;
    document.getElementById('cgpaError').style.display='inline';
  }

  return success;//always return a value true if all fields are filled false if anyone is empty
}
