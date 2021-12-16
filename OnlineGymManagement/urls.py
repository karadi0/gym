from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gym.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('user_home',User_Home,name="user_home"),
    path('trainer_home',Trainer_Home,name="trainer_home"),
    path('login_user',Login_User,name="login_user"),
    path('contact',Contact,name="contact"),
    path('about',About,name="about"),
    path('edit_profile',Edit_Profile,name="edit_profile"),
    path('admin_profile',admin_profile,name="admin_profile"),
    path('logout', Logout, name="logout"),
    path('login_admin',Login_Admin,name="login_admin"),
    path('signup', Signup_User,name="signup"),
    path('signup_trainer', Signup_Trainer,name="signup_trainer"),
    path('trainer', trainr,name="trainer"),
    path('tips', tips,name="tips"),
    path('join_batch(<int:pid>)', join_batch,name="join_batch"),
    path('add_diet', add_diet,name="add_diet"),
    path('view_diet', View_diet,name="view_diet"),
    path('view_diet1', View_diet1,name="view_diet1"),
    path('dashboard', Trainer_Home,name="dashboard"),
    path('dashboard1', User_Home,name="dashboard1"),
    path('change_password',Change_Password,name="change_password"),
    path('admin_home', Admin_Home,name="admin_home"),
    path('view_package', View_Package,name="view_package"),
    path('new_trainer', View_New_Trainer,name="new_trainer"),
    path('all_trainer', View_All_Trainer,name="all_trainer"),
    path('all_member', View_All_Member,name="all_member"),
    path('add_product', Add_Product,name="add_product"),
    path('status(<int:pid>)', Change_status, name='status'),
    path('status1(<int:pid>)', Change_status1, name='status1'),
    path('add_package', add_package,name="add_package"),
    path('view_order', View_Order,name="view_order"),
    path('my_batch', my_batch,name="my_batch"),
    path('all_memeber1', all_memeber1,name="all_memeber1"),
    path('view_attendance1', View_Attendance1,name="view_attendance1"),
    path('activity', Activity1,name="activity"),
    path('product1', product1,name="product1"),
    path('add_cart(?P<int:pid>)', Add_Cart, name='add_cart'),
    path('edit_package(<int:pid>)', edit_package, name='edit_package'),
    path('edit_batch(<int:pid>)', Edit_Batch, name='edit_batch'),
    path('edit_activity(<int:pid>)', Edit_Activity, name='edit_activity'),
    path('edit_trainer(<int:pid>)', Edit_Trainer, name='edit_trainer'),
    path('edit_member(<int:pid>)', Edit_Member, name='edit_member'),
    path('edit_diet(<int:pid>)', edit_diet, name='edit_diet'),
    path('edit_product(<int:pid>)', Edit_Product, name='edit_product'),
    path('delete_product(<int:pid>)', delete_product, name='delete_product'),
    path('delete_batch(<int:pid>)', delete_batch, name='delete_batch'),
    path('delete_diet(<int:pid>)', delete_diet, name='delete_diet'),
    path('delete_trainer(<int:pid>)', delete_trainer, name='delete_trainer'),
    path('delete_order(<int:pid>)', delete_order, name='delete_order'),
    path('delete_member(<int:pid>)', delete_member, name='delete_member'),
    path('delete_all_activity(<int:pid>)', delete_all_activity, name='delete_all_activity'),
    path('delete_activity(<int:pid>)', delete_activity, name='delete_activity'),
    path('delete_tips(<int:pid>)', delete_tips, name='delete_tips'),
    path('delete_package(<int:pid>)', delete_package, name='delete_package'),
    path('booking_detail/(<str:pid>)/(<int:bid>)', booking_detail, name='booking_detail'),
    path('order_detail/(<str:pid>)/(<int:bid>)', View_Order_Detail, name='order_detail'),
    path('booking(?P<str:pid>)', Booking_order, name="booking"),
    path('cart', view_cart, name='cart'),
    path('profile', profile, name='profile'),
    path('thanks_message', thanks_message, name='thanks_message'),
    path('remove_cart(?P<int:pid>)', remove_cart, name='remove_cart'),
    path('view_member_detail(<int:pid>)', view_member_detail,name="view_member_detail"),
    path('search_member(<str:pid>)', search_member,name="search_member"),
    path('add_tips', Add_Tips,name="add_tips"),
    path('my_activity', my_activity,name="my_activity"),
    path('my_order', My_Order,name="my_order"),
    path('add_batch', Add_Batch,name="add_batch"),
    path('add_activity', Add_Activity,name="add_activity"),
    path('add_trainer_activity', add_trainer_activity,name="add_trainer_activity"),
    path('view_attendance', View_Attendance,name="view_attendance"),
    path('add_attendance(<int:pid>)', add_attendance,name="add_attendance"),
    path('view_attendance_detail(<int:pid>)', View_Attendance_Detail,name="view_attendance_detail"),
    path('view_product', View_Product,name="view_product"),
    path('view_all_activity', view_all_activity,name="view_all_activity"),
    path('view_activity', view_activity,name="view_activity"),
    path('view_tips', View_Tips,name="view_tips"),
    path('view_all_batch', View_All_Batch,name="view_all_batch"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
