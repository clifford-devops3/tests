<template>
  <div>
    <h2>Implement jQuery DataTable in Vue Js</h2>
    <table class="table" id="datatable">
      <thead>
        <tr>
          <th>ID</th>
          <th>Product Title</th>
          <th>Product Price</th>
          <th>Created On</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in products" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.product_title }}</td>
          <td>{{ item.product_price }}</td>
          <td>{{ item.created_at }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import "jquery/dist/jquery.min.js";
import "bootstrap/dist/css/bootstrap.min.css";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import 'datatables.net-buttons/js/dataTables.buttons.js'
import 'datatables.net-buttons/js/buttons.html5.js'
import 'datatables.net-buttons/js/buttons.print.js'
import $ from "jquery";
export default {
  mounted() {
    $("#datatable").DataTable({
      buttons: [
        {
          extend: "pdf",
          text: "Save current page",
          exportOptions: {
            modifier: {
              page: "current",
            },
          },
        },
      ],
    });
  },
  data: function () {
    return {
      products: [
        {
          id: 10,
          product_title: "Car",
          product_price: 500,
          created_at: "20-12-2021",
        },
        {
          id: 11,
          product_title: "Van",
          product_price: 600,
          created_at: "20-12-2021",
        },
        {
          id: 12,
          product_title: "Truck",
          product_price: 700,
          created_at: "20-12-2021",
        },
        {
          id: 13,
          product_title: "SUV",
          product_price: 1000,
          created_at: "20-12-2021",
        },
      ],
    };
  },
};
</script>