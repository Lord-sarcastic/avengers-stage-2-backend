connect_to_database.php
<?php
mysql_connect("localhost","your_username","your_password") or die(mysql_error());
mysql_select_db("your_database");
?>
login.php
<?php
include 'connect_to_database.php'; //connect the connection page
if(empty($_SESSION)) // if the session not yet started
   session_start();


if(isset($_SESSION['username'])) { // if already login
   header("location: home.php"); // send to home page
   exit; 
}

?>
<html>
<head></head>
<body>
<form action = "login_proccess.php" method = "post">
Username: <input type="text" name="username" /><br />
Password: <input type="password" name="password" /><br />
<input type = "submit" name="submit" value="login" />
</form>
</body>
</html>
login_proccess.php
<?php
include 'connect_to_database.php'; //connect the connection page
 
if(empty($_SESSION)) // if the session not yet started
   session_start();
if(!isset($_POST['submit'])) { // if the form not yet submitted
   header("Location: login.php");
   exit;
}
//check if the username entered is in the database.
$test_query = "SELECT * FROM table_name WHERE username_field = '".$_POST[username]."'";
$query_result = mysql_query($test_query);
//conditions
if(mysql_num_rows($query_result)==0) {
//if username entered not yet exists
    echo "The username you entered is invalid.";
}else {
//if exists, then extract the password.
    while($row_query = mysql_fetch_array($query_result)) {
        // check if password are equal
        if($row_query['password_field']==$_POST['password']){
            $_SESSION['password'] = $_POST['password'];
            header("Location: home.php");
            exit;
        } else{ // if not
            echo "Invalid Password";
        }
    }
}
?>
home.php
<?php
include 'connect_to_database.php'; //connect the connection page

if(empty($_SESSION)) // if the session not yet started
   session_start();

if(!isset($_SESSION['username'])) { //if not yet logged in
   header("Location: login.php");// send to login page
   exit;
}
?>
<html>
<body>
Welcome <?php echo $_SESSION['username']; ?>,
 <a href="logout.php">logout</a>
</body>
</html>
logout.php
<?php
session_start();
unset($_SESSION['username']);
session_destroy();

header("Location: login.php");
exit;
?>
