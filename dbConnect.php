<?php

$host = "mysql43.mydevil.net";
$db_name = "m1121_alibestof";
$db_user = "m1121_kemotto";
$db_password = "Beatka1190";

$table_products="products";

$connection = @new mysqli($host, $db_user, $db_password, $db_name);

if($connection->connect_errno != 0) {
    echo <<< _END
<br/>
<label>Error: $connection->connect_errno</label>
_END;
    exit();
}
?>