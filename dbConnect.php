<?php

$host = "localhost";
$db_user = "kemotto_user";
$db_password = "db_Beatka";
$db_name = "kemotto_alibestof";

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