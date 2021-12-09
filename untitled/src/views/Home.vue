<template>
  <div>
    <!-- Main wrapper  -->
    <div id="main-wrapper">
      <!-- header header  -->
      <div class="header">
        <nav class="navbar top-navbar navbar-expand-md navbar-light">
          <!-- Logo -->
          <div class="navbar-header">
            <a class="navbar-brand" href="index.html">
              <!-- Logo icon -->
              <b><img src="../../public/images/logo.png" alt="homepage" class="dark-logo"/></b>
              <!--End Logo icon -->
              <!-- Logo text -->
              <!--              <span><img src="../public/images/logo-text.png" alt="homepage" class="dark-logo"/></span>-->
            </a>
          </div>
          <!-- End Logo -->
          <div class="navbar-collapse">

            <!-- User profile and search -->
            <ul class="navbar-nav my-lg-0">

              <!-- Search -->
              <li class="nav-item hidden-sm-down search-box"><a class="nav-link hidden-sm-down text-muted  "
                                                                href="javascript:void(0)"><i
                  class="ti-search"></i></a>
                <form class="app-search">
                  <input type="text" class="form-control" placeholder="Search here"> <a class="srh-btn"><i
                    class="ti-close"></i></a></form>
              </li>

              <!-- Profile -->
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle text-muted  " href="#" data-toggle="dropdown"
                   aria-haspopup="true" aria-expanded="false"><img src="../../public/images/users/5.jpg" alt="user"
                                                                   class="profile-pic"/></a>
                <div class="dropdown-menu dropdown-menu-right animated zoomIn">
                  <ul class="dropdown-user">
                    <li><a href="#"><i class="ti-user"></i> Профиль</a></li>
                    <li><a href="#"><i class="ti-settings"></i> Настройки</a></li>
                    <li><a href="#"><i class="fa fa-power-off"></i> Выход</a></li>
                  </ul>
                </div>
              </li>
            </ul>
          </div>
          <Navbar
              :is_auth="is_auth"
          />
        </nav>
      </div>
      <!-- End header header -->

      <!-- Page wrapper  -->
      <div class="page-wrapper">
        <!-- Bread crumb -->
        <div class="row page-titles">
          <div class="col-md-5 align-self-center">
            <h3 class="text-primary">Панель администратора</h3></div>
          <div class="col-md-7 align-self-center">
            <ol class="breadcrumb">
              <li class="breadcrumb-item"><a href="javascript:void(0)">Домой</a></li>
              <li class="breadcrumb-item active">Панель администратора</li>
            </ol>
          </div>
        </div>
        <!-- End Bread crumb -->
        <!-- Container fluid  -->
        <div class="container-fluid">
          <!-- Start Page Content -->
          <div class="row">
            <div class="col-md-3">
              <div class="card p-30">
                <div class="media">
                  <div class="media-left meida media-middle">
                    <span><i class="fa fa-check-square-o f-s-40 color-primary"></i></span>
                  </div>
                  <div class="media-body media-text-right">
                    <h2>568120</h2>
                    <p class="m-b-0">Всего объектов</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-3">
              <div class="card p-30">
                <div class="media">
                  <div class="media-left meida media-middle">
                    <span><i class="fa fa-file-text f-s-40 color-success"></i></span>
                  </div>
                  <div class="media-body media-text-right">
                    <h2>1178</h2>
                    <p class="m-b-0">XML файлов</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-3">
              <div class="card p-30">
                <div class="media">
                  <div class="media-left meida media-middle">
                    <span><i class="fa fa-archive f-s-40 color-warning"></i></span>
                  </div>
                  <div class="media-body media-text-right">
                    <h2>425</h2>
                    <p class="m-b-0">Архивов</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-3">
              <div class="card p-30">
                <div class="media">
                  <div class="media-left meida media-middle">
                    <span><i class="fa fa-bug f-s-40 color-danger"></i></span>
                  </div>
                  <div class="media-body media-text-right">
                    <h2>47</h2>
                    <p class="m-b-0">Вредоносные</p>
                  </div>
                </div>
              </div>
            </div>
          </div>


          <div class="col-lg-12">
            <div class="card">
              <div class="card-title">
                <h4>Статистика проверки вложений </h4>
              </div>
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table">
                    <thead>
                    <tr>
                      <th>#</th>
                      <th>Дата</th>
                      <th>Название XML</th>
                      <th>Вложений</th>
                      <th>Размер</th>
                      <th>Вредоносных объектов</th>
                      <th>Статус</th>
                      <th>Действие</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(file, i) in input_files" :key="i">
                      <td>
                        {{ i }}
                      </td>
                      <td>{{ file.datetime }}</td>
                      <td><a href="">{{ file.name }}</a></td>
                      <td><span>{{ file.files }}</span></td>
                      <td><span>{{ file.size }} кб</span></td>
                      <td><span
                          v-bind:class="{
                        'badge-danger':file.danger,
                        'badge-success': !file.danger,
                      }"
                          class="badge ">{{ file.danger }}</span></td>
                      <td><span
                          v-bind:class="{
                        'badge-warning':file.success!=='Завершено',
                        'badge-success':file.success==='Завершено',
                      }"
                          class="badge">{{ file.success }}</span></td>
                      <td>
                        <a :href="file.url" class="btn btn-success btn-sm m-b-10 m-l-5">Скачать
                        </a>
                      </td>

                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="pagination">
              <a href="#">&laquo;</a>
              <a href="#">1</a>
              <a href="#">2</a>
              <a href="#">3</a>
              <a href="#">4</a>
              <a href="#">5</a>
              <a href="#">6</a>
              <a href="#">&raquo;</a>
            </div>

          </div>

          <div class="col-lg-12">
            <div class="card">
              <div class="card-title">
                <h4>Вложения в XML файле file1.xml</h4>

              </div>
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-hover ">
                    <thead>
                    <tr>
                      <th>#</th>
                      <th>Дата</th>
                      <th>Название</th>
                      <th>Статус</th>
                      <th>sha256 хэш</th>
                      <th>Действие</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(file, i) in output_files" :key="i">
                      <th scope="row">{{i}}</th>
                      <td>{{ file.datetime }}</td>
                      <td>{{ file.name }}</td>
                      <td><span
                          v-bind:class="{
                              'badge-danger':file.status === 'Вредоносный',
                              'badge-success': file.status !== 'Вредоносный'
                          }"
                          class="badge badge-success">{{ file.status }}</span></td>
                      <td>{{ file.sha }}</td>
                      <td>
                        <a :href="file.url" class="btn btn-success btn-sm m-b-10 m-l-5">Скачать
                        </a>
                      </td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {mapActions, mapGetters} from "vuex";
import Navbar from "../components/common/Navbar";

export default {
  name: 'App',
  data() {
    return {
      input_files: [
        {
          datetime: '21.11.2021, 20:35',
          name: 'file5.xml',
          files: '21',
          size: '5204',
          danger: 1,
          success: 'Завершено',
          url:'#'
        },
        {
          datetime: '21.11.2021, 19:22',
          name: 'file4.xml',
          files: '19',
          size: '9984',
          danger: 1,
          success: 'Завершено',
          url:'#'
        },
        {
          datetime: '21.11.2021, 17:40',
          name: 'file3.xml',
          files: '30',
          size: '8091',
          danger: 0,
          success: 'Завершено',
          url:'#'
        },
        {
          datetime: '21.11.2021, 18:47',
          name: 'file2.xml',
          files: '114',
          size: '100204',
          danger: 2,
          success: 'На проверке',
          url:'#'
        },
        {
          datetime: '21.11.2021, 15:14',
          name: 'file1.xml',
          files: '21',
          size: '5204',
          danger: 1,
          success: 'Завершено',
          url:'#'
        },
      ],
      output_files:[
        {
          datetime: '21.11.2021, 18:47',
          name: 'image.jpg',
          status: 'Безопасный',
          sha: 'b2974c63ac891dbc7204da36000fa7afdf47635b',
          url:'#'
        },
        {
          datetime: '21.11.2021, 18:47',
          name: 'document.pdf',
          status: 'Безопасный',
          sha: '66f4536970c760df4b35aaa5dcd63a59885d536e',
          url:'#'
        },
        {
          datetime: '21.11.2021, 18:47',
          name: 'обнолвение.exe',
          status: 'Вредоносный',
          sha: '9e27f726fc19ec7065c3207d6ee720c5d4fd5bb7',
          url:'#'
        },
        {
          datetime: '21.11.2021, 18:47',
          name: 'doc.xlsx',
          status: 'Вредоносный',
          sha: '9e27f726fc19ec7065c3207d6ee720c5d4fd5bb7',
          url:'#'
        },
      ]
    }
  },
  props: [
    'is_auth'
  ],
  components: {
    Navbar
  },
  methods: {
    ...mapActions(['verifyToken', 'activation', 'authorization', 'logout', 'setUser', 'createUser']),
  },
  computed: {
    ...mapGetters(['getAuth']),
  },
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300i,400,600,700,800');
@import url(../../public/css/lib/bootstrap/bootstrap.min.css);
@import url(../../public/icons/font-awesome/css/font-awesome.min.css);
@import url(../../public/icons/simple-line-icons/css/simple-line-icons.css);
@import url(../../public/icons/weather-icons/css/weather-icons.min.css);
@import url(../../public/icons/linea-icons/linea.css);
@import url(../../public/icons/themify-icons/themify-icons.css);
@import url(../../public/icons/flag-icon-css/flag-icon.min.css);
@import url(../../public/icons/material-design-iconic-font/css/materialdesignicons.min.css);

html {
  position: relative;
  min-height: 100%;
  background: #ffffff;
}

a:focus,
a:hover {
  text-decoration: none;
}

a.link {
  color: #455a64;
}

a.link:focus,
a.link:hover {
  color: #1976d2;
}

.img-responsive,
.carousel.vertical .carousel-inner > .item > img,
.carousel.vertical .carousel-inner > .item > a > img {
  width: 100%;
  height: auto;
  display: inline-block;
}

.img-rounded {
  border-radius: 4px;
}


h1,
h2,
h3,
h4,
h5,
h6 {
  color: #455a64;
  font-weight: 400;
}

h1 {
  line-height: 40px;
  font-size: 36px;
}

h2 {
  line-height: 36px;
  font-size: 24px;
}

h3 {
  line-height: 30px;
  font-size: 21px;
}

h4 {
  line-height: 22px;
  font-size: 18px;
}

h5 {
  line-height: 18px;
  font-size: 16px;
  font-weight: 400;
}

h6 {
  line-height: 16px;
  font-size: 14px;
  font-weight: 400;
}

.display-5 {
  font-size: 3rem;
}

.display-6 {
  font-size: 36px;
}

.box {
  border-radius: 4px;
  padding: 10px;
}

.preloader {
  width: 100%;
  height: 100%;
  top: 0;
  position: fixed;
  z-index: 99999;
  background: #fff;
}

.preloader .cssload-speeding-wheel {
  position: absolute;
  top: calc(46.5%);
  left: calc(46.5%);
}

#main-wrapper {
  width: 100%;
}

.bg-white .card {
  box-shadow: none;
}

.box-shadow {
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05) !important;
}

.dropzone {
  border: 1px dashed #b1b8bb;
}

.boxed #main-wrapper {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  -webkit-box-shadow: 0 0 60px rgba(0, 0, 0, 0.1);
  box-shadow: 0 0 60px rgba(0, 0, 0, 0.1);
}

.boxed #main-wrapper .sidebar-footer {
  position: absolute;
}

.boxed #main-wrapper .footer {
  display: none;
}

.page-wrapper {
  background: #fafafa;
  padding-bottom: 60px;
}

.container-fluid {
  padding: 0 30px 25px;
}

@media (min-width: 1024px) {
  .page-wrapper {
    margin-left: 0px;
  }

  .footer {
    left: 240px;
  }
}

@media (max-width: 1023px) {
  .page-wrapper {
    margin-left: 60px;
    -webkit-transition: 0.2s ease-in;
    -o-transition: 0.2s ease-in;
    transition: 0.2s ease-in;
  }

  .footer {
    left: 60px;
  }

  .widget-app-columns {
    -webkit-column-count: 1;
    -moz-column-count: 1;
    column-count: 1;
  }
}

.hide {
  display: none;
}

.img-circle {
  border-radius: 100%;
}

.radius {
  border-radius: 4px;
}

.text-white {
  color: #ffffff !important;
}

.text-danger {
  color: #ef5350 !important;
}

.text-muted {
  color: #99abb4 !important;
}

.text-warning {
  color: #ffb22b !important;
}

.text-success {
  color: #26dad2 !important;
}

.text-info {
  color: #1976d2 !important;
}

.text-inverse {
  color: #2f3d4a !important;
}

.text-blue {
  color: #02bec9;
}

.text-purple {
  color: #7460ee;
}

.text-primary {
  color: #5c4ac7;
}

.text-megna {
  color: #00897b;
}

.text-dark {
  color: #67757c;
}

.text-themecolor {
  color: #1976d2;
}

.bg-primary {
  background-color: #5c4ac7 !important;
}

.bg-success {
  background-color: #26dad2 !important;
}

.bg-info {
  background-color: #1976d2 !important;
}

.bg-warning {
  background-color: #ffb22b !important;
}

.bg-danger {
  background-color: #ef5350 !important;
}

.bg-megna {
  background-color: #00897b;
}

.bg-theme {
  background-color: #1976d2;
}

.bg-inverse {
  background-color: #2f3d4a;
}

.bg-purple {
  background-color: #7460ee;
}

.bg-light-part {
  background-color: rgba(0, 0, 0, 0.02);
}

.bg-light-primary {
  background-color: #f1effd;
}

.bg-light-success {
  background-color: #e8fdeb;
}

.bg-light-info {
  background-color: #cfecfe;
}

.bg-light-extra {
  background-color: #ebf3f5;
}

.bg-light-warning {
  background-color: #fff8ec;
}

.bg-light-danger {
  background-color: #f9e7eb;
}

.bg-light-inverse {
  background-color: #f6f6f6;
}

.bg-light {
  background-color: #f2f4f8;
}

.bg-white {
  background-color: #ffffff;
}

@media (min-width: 1600px) {
  .col-xlg-1,
  .col-xlg-10,
  .col-xlg-11,
  .col-xlg-12,
  .col-xlg-2,
  .col-xlg-3,
  .col-xlg-4,
  .col-xlg-5,
  .col-xlg-6,
  .col-xlg-7,
  .col-xlg-8,
  .col-xlg-9 {
    float: left;
  }

  .col-xlg-12 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 100%;
    -ms-flex: 0 0 100%;
    flex: 0 0 100%;
    max-width: 100%;
  }

  .col-xlg-11 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 91.66666667%;
    -ms-flex: 0 0 91.66666667%;
    flex: 0 0 91.66666667%;
    max-width: 91.66666667%;
  }

  .col-xlg-10 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 83.33333333%;
    -ms-flex: 0 0 83.33333333%;
    flex: 0 0 83.33333333%;
    max-width: 83.33333333%;
  }

  .col-xlg-9 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 75%;
    -ms-flex: 0 0 75%;
    flex: 0 0 75%;
    max-width: 75%;
  }

  .col-xlg-8 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 66.66666667%;
    -ms-flex: 0 0 66.66666667%;
    flex: 0 0 66.66666667%;
    max-width: 66.66666667%;
  }

  .col-xlg-7 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 58.33333333%;
    -ms-flex: 0 0 58.33333333%;
    flex: 0 0 58.33333333%;
    max-width: 58.33333333%;
  }

  .col-xlg-6 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 50%;
    -ms-flex: 0 0 50%;
    flex: 0 0 50%;
    max-width: 50%;
  }

  .col-xlg-5 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 41.66666667%;
    -ms-flex: 0 0 41.66666667%;
    flex: 0 0 41.66666667%;
    max-width: 41.66666667%;
  }

  .col-xlg-4 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 33.33333333%;
    -ms-flex: 0 0 33.33333333%;
    flex: 0 0 33.33333333%;
    max-width: 33.33333333%;
  }

  .col-xlg-3 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 25%;
    -ms-flex: 0 0 25%;
    flex: 0 0 25%;
    max-width: 25%;
  }

  .col-xlg-2 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 16.66666667%;
    -ms-flex: 0 0 16.66666667%;
    flex: 0 0 16.66666667%;
    max-width: 16.66666667%;
  }

  .col-xlg-1 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 8.33333333%;
    -ms-flex: 0 0 8.33333333%;
    flex: 0 0 8.33333333%;
    max-width: 8.33333333%;
  }

  .col-xlg-pull-12 {
    right: 100%;
  }

  .col-xlg-pull-11 {
    right: 91.66666667%;
  }

  .col-xlg-pull-10 {
    right: 83.33333333%;
  }

  .col-xlg-pull-9 {
    right: 75%;
  }

  .col-xlg-pull-8 {
    right: 66.66666667%;
  }

  .col-xlg-pull-7 {
    right: 58.33333333%;
  }

  .col-xlg-pull-6 {
    right: 50%;
  }

  .col-xlg-pull-5 {
    right: 41.66666667%;
  }

  .col-xlg-pull-4 {
    right: 33.33333333%;
  }

  .col-xlg-pull-3 {
    right: 25%;
  }

  .col-xlg-pull-2 {
    right: 16.66666667%;
  }

  .col-xlg-pull-1 {
    right: 8.33333333%;
  }

  .col-xlg-pull-0 {
    right: auto;
  }

  .col-xlg-push-12 {
    left: 100%;
  }

  .col-xlg-push-11 {
    left: 91.66666667%;
  }

  .col-xlg-push-10 {
    left: 83.33333333%;
  }

  .col-xlg-push-9 {
    left: 75%;
  }

  .col-xlg-push-8 {
    left: 66.66666667%;
  }

  .col-xlg-push-7 {
    left: 58.33333333%;
  }

  .col-xlg-push-6 {
    left: 50%;
  }

  .col-xlg-push-5 {
    left: 41.66666667%;
  }

  .col-xlg-push-4 {
    left: 33.33333333%;
  }

  .col-xlg-push-3 {
    left: 25%;
  }

  .col-xlg-push-2 {
    left: 16.66666667%;
  }

  .col-xlg-push-1 {
    left: 8.33333333%;
  }

  .col-xlg-push-0 {
    left: auto;
  }

  .offset-xlg-12 {
    margin-left: 100%;
  }

  .offset-xlg-11 {
    margin-left: 91.66666667%;
  }

  .offset-xlg-10 {
    margin-left: 83.33333333%;
  }

  .offset-xlg-9 {
    margin-left: 75%;
  }

  .offset-xlg-8 {
    margin-left: 66.66666667%;
  }

  .offset-xlg-7 {
    margin-left: 58.33333333%;
  }

  .offset-xlg-6 {
    margin-left: 50%;
  }

  .offset-xlg-5 {
    margin-left: 41.66666667%;
  }

  .offset-xlg-4 {
    margin-left: 33.33333333%;
  }

  .offset-xlg-3 {
    margin-left: 25%;
  }

  .offset-xlg-2 {
    margin-left: 16.66666667%;
  }

  .offset-xlg-1 {
    margin-left: 8.33333333%;
  }

  .offset-xlg-0 {
    margin-left: 0;
  }
}

.col-xlg-1,
.col-xlg-10,
.col-xlg-11,
.col-xlg-12,
.col-xlg-2,
.col-xlg-3,
.col-xlg-4,
.col-xlg-5,
.col-xlg-6,
.col-xlg-7,
.col-xlg-8,
.col-xlg-9 {
  position: relative;
  min-height: 1px;
  padding-right: 15px;
  padding-left: 15px;
}

.input-group-addon [type=checkbox]:checked,
.input-group-addon [type=checkbox]:not(:checked),
.input-group-addon [type=radio]:checked,
.input-group-addon [type=radio]:not(:checked) {
  position: initial;
  opacity: 1;
}

.invisible {
  visibility: hidden !important;
}

.hidden-xs-up {
  display: none !important;
}

@media (max-width: 575px) {
  .hidden-xs-down {
    display: none !important;
  }
}

@media (min-width: 576px) {
  .hidden-sm-up {
    display: none !important;
  }
}

@media (max-width: 767px) {
  .hidden-sm-down {
    display: none !important;
  }
}

@media (min-width: 768px) {
  .hidden-md-up {
    display: none !important;
  }
}

@media (max-width: 991px) {
  .hidden-md-down {
    display: none !important;
  }
}

@media (min-width: 992px) {
  .hidden-lg-up {
    display: none !important;
  }
}

@media (max-width: 1199px) {
  .hidden-lg-down {
    display: none !important;
  }
}

@media (min-width: 1200px) {
  .hidden-xl-up {
    display: none !important;
  }
}

.hidden-xl-down {
  display: none !important;
}

@media (min-width: 1650px) {
  .widget-app-columns {
    -webkit-column-count: 3;
    -moz-column-count: 3;
    column-count: 3;
  }

  .campaign {
    height: 365px !important;
  }
}

@media (max-width: 1370px) {
  .widget-app-columns {
    -webkit-column-count: 2;
    -moz-column-count: 2;
    column-count: 2;
  }
}

a,
button {
  outline: none !important;
  text-decoration: none !important;
  color: #99abb4;
  transition: all 0.2s ease 0s;
}

a.active,
button.active,
a:focus,
button:focus,
a:hover,
button:hover {
  color: #252525;
  outline: none !important;
  text-decoration: none !important;
}

ul {
  padding: 0;
  margin: 0;
}

li {
  list-style: none;
}

p {
  font-family: 'Poppins', sans-serif;
  color: #99abb4;
}

.media-body {
  vertical-align: middle;
}

.media-body span {
  font-size: 10px;
  color: #4680ff;
}

.media-body p {
  color: #99abb4;
  line-height: 15px;
}

.header {
  position: relative;
  z-index: 50;
  background: #fff;
  box-shadow: 1px 0 5px rgba(0, 0, 0, 0.1);
}

.header .top-navbar {
  min-height: 50px;
  padding: 0 15px 0 0;
  margin-left: 40px;
}

.header .top-navbar .dropdown-toggle:after {
  display: none;
}

.header .top-navbar .navbar-header {
  line-height: 45px;
  text-align: center;
  background: #fff;
}

.header .top-navbar .navbar-header .navbar-brand {
  margin-right: 0;
  padding-bottom: 0;
  padding-top: 0;
}

.header .top-navbar .navbar-header .navbar-brand .light-logo {
  display: none;
}

.header .top-navbar .navbar-header .navbar-brand b {
  line-height: 60px;
  display: inline-block;
}

.header .top-navbar .navbar-nav > .nav-item > .nav-link {
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  font-size: 15px;
  line-height: 40px;
}

.header .top-navbar .navbar-nav > .nav-item.show {
  background: rgba(0, 0, 0, 0.05);
}

.header .top-navbar .mailbox {
  width: 300px;
}

.header .top-navbar .mailbox ul {
  padding: 0;
}

.header .top-navbar .mailbox ul li {
  list-style: none;
}

.header .profile-pic {
  width: 30px;
  border-radius: 100%;
}

.header .dropdown-menu {
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
  -webkit-box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
  -moz-box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
  border-color: rgba(120, 130, 140, 0.13);
}

.header .dropdown-menu .dropdown-item {
  padding: 7px 1.5rem;
}

.header ul.dropdown-user {
  padding: 0;
  min-width: 175px;
}

.header ul.dropdown-user li {
  list-style: none;
  padding: 0;
  margin: 0;
}

.header ul.dropdown-user li .dw-user-box {
  padding: 10px 15px;
}

.header ul.dropdown-user li .dw-user-box .u-img {
  width: 70px;
  display: inline-block;
  vertical-align: top;
}

.header ul.dropdown-user li .dw-user-box .u-img img {
  width: 100%;
  border-radius: 5px;
}

.header ul.dropdown-user li .dw-user-box .u-text {
  display: inline-block;
  padding-left: 10px;
}

.header ul.dropdown-user li .dw-user-box .u-text h4 {
  margin: 0;
  font-size: 15px;
}

.header ul.dropdown-user li .dw-user-box .u-text p {
  margin-bottom: 2px;
  font-size: 12px;
}

.header ul.dropdown-user li .dw-user-box .u-text .btn {
  color: #ffffff;
  padding: 5px 10px;
  display: inline-block;
}

.header ul.dropdown-user li .dw-user-box .u-text .btn:hover {
  background: #e6294b;
}

.header ul.dropdown-user li a {
  padding: 9px 15px;
  display: block;
  color: #67757c;
}

.header ul.dropdown-user li a:hover {
  background: #f2f4f8;
  color: #1976d2;
  text-decoration: none;
}

.header ul.dropdown-user li.divider {
  height: 1px;
  margin: 9px 0;
  overflow: hidden;
  background-color: rgba(120, 130, 140, 0.13);
}

.search-box .app-search {
  position: absolute;
  margin: 0;
  display: block;
  z-index: 110;
  width: 100%;
  top: -1px;
  -webkit-box-shadow: 2px 0 10px rgba(0, 0, 0, 0.2);
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.2);
  display: none;
  left: 0;
}

.search-box .app-search input {
  width: 100.5%;
  padding: 20px 40px 20px 20px;
  border-radius: 0;
  font-size: 17px;
  height: 70px;
  -webkit-transition: 0.5s ease-in;
  -o-transition: 0.5s ease-in;
  transition: 0.5s ease-in;
}

.search-box .app-search input:focus {
  border-color: #ffffff;
}

.search-box .app-search .srh-btn {
  position: absolute;
  top: 23px;
  cursor: pointer;
  background: #ffffff;
  width: 15px;
  height: 15px;
  right: 20px;
  font-size: 14px;
}

.header-search {
  float: right;
  margin-left: 15px;
  position: relative;
}

.header-search .form-control {
  height: 36px;
  width: 250px;
  border-radius: 5px;
  font-size: 14px;
}

.header-search i {
  position: absolute;
  right: 5px;
  top: 5px;
  cursor: pointer;
  height: 30px;
  padding: 5px;
  width: 30px;
}

.media-text-right {
  text-align: right;
}

.media-text-left {
  text-align: left;
}

.boxshadow-none {
  box-shadow: none;
}

.h2,
.h3,
.h4,
.h5,
.h6,
h1,
h2,
h3,
h4,
h5,
h6.h1 {
  color: #455a64;
}

.dib {
  display: inline-block;
}

.table > thead > tr > th {
  border-bottom: 1px solid #e7e7e7;
  font-weight: 600;
}

.table > tbody > tr > td, .table > tbody > tr > th, .table > tfoot > tr > td, .table > tfoot > tr > th, .table > thead > tr > td, .table > thead > tr > th {
  line-height: 32px;
  vertical-align: top;
}

.table thead th {
  vertical-align: bottom;
  border-bottom: 2px solid #dee2e6;
}

.table td, .table th {
  padding: 0.55rem;
}

.table td, .table th {
  padding: .75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

thead tr th {
  color: #455a64;
  font-weight: 500;
}

th {
  text-align: inherit;
}

.breadcrumb {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 0.75rem 1rem;
  margin-bottom: 0;
  list-style: none;
  background-color: #e9ecef;
  border-radius: 0.25rem;
}

.breadcrumb-item + .breadcrumb-item::before {
  display: inline-block;
  padding-right: 0.5rem;
  padding-left: 0.5rem;
  color: #6c757d;
  content: "/";
}

.breadcrumb-item + .breadcrumb-item:hover::before {
  text-decoration: underline;
}

.breadcrumb-item + .breadcrumb-item:hover::before {
  text-decoration: none;
}

.breadcrumb-item.active {
  color: #6c757d;
}

.pagination {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  padding-left: 0;
  list-style: none;
  border-radius: 0.25rem;
}

.navbar-expand-md .navbar-collapse {
  display: -webkit-box !important;
  display: -ms-flexbox !important;
  display: flex !important;
  -ms-flex-preferred-size: auto;
  flex-basis: auto;
}

.navbar-collapse {
  -ms-flex-preferred-size: 100%;
  flex-basis: 100%;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.navbar-light .navbar-brand {
  color: rgba(0, 0, 0, .9);
}

.navbar-brand {
  font-size: 1.25rem;
  line-height: inherit;
  white-space: nowrap;
}

.page-titles h3 {
  margin-bottom: 0;
  margin-top: 0;
  margin-left: 30px;
}

.color-primary, .text-primary {
  color: #4680ff;
}

.page-titles .breadcrumb .breadcrumb-item.active {
  color: #99abb4;
}

.page-titles .breadcrumb li {
  margin-top: 0;
  margin-bottom: 0;
}

.breadcrumb-item.active {
  color: #6c757d;
}

.header .profile-pic {
  width: 30px;
  border-radius: 100%;
}

img {
  vertical-align: middle;
  border-style: none;
}

.color-warning, .text-warning {
  color: #ffb64d;
}

.color-success, .text-success {
  color: #26dad2;
}

.color-danger, .text-danger {
  color: #fc6180;
}

.color-primary, .text-primary {
  color: #4680ff;
}

.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: 14px;
  font-size: 54px;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.text-primary {
  color: #007bff !important;
}

p {
  font-family: 'Poppins', sans-serif;
  color: #99abb4;
  margin-top: 0;
  margin-bottom: 0;
}

.media-body p {
  color: #99abb4;
  line-height: 15px;
}

.card {
  background: #ffffff none repeat scroll 0 0;
  margin: 15px 0;
  padding: 20px;
  border: 0 solid #e7e7e7;
  border-radius: 5px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
}

.card-title {
  font-weight: 500;
  font-size: 18px;
  line-height: 22px;
}

.card-title {
  margin-bottom: .75rem;
}

.table .badge {
  text-transform: uppercase;
}

.badge-success {
  background-color: #26dad2;
}

.badge-warning {
  background-color: #ffb22b;
}

.badge-success {
  color: #fff;
  background-color: #28a745;
}

.badge {
  display: inline-block;
  padding: .25em .4em;
  font-size: 75%;
  font-weight: 700;
  line-height: 1;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25rem;
}

.badge-danger {
  background-color: #ef5350;
}

.badge {
  font-weight: 400;
}

.badge-danger {
  color: #fff;
  background-color: #dc3545;
}

.pagination {
  display: inline-block;
}

.pagination a {
  color: black;
  float: left;
  padding: 8px 16px;
  text-decoration: none;
}

.header ul.dropdown-user li a {
  padding: 9px 15px;
  display: block;
  color: #67757c;
}

a, button {
  outline: none !important;
  text-decoration: none !important;
  color: #99abb4;
  transition: all 0.2s ease 0s;
}


</style>