<?php

$host = "localhost";
$db_name = "kemotto_alibestof";
$db_user = "root";
$db_password = "123";

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