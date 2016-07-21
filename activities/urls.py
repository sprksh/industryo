from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^workplace_data$', 'workplace.views.workplace_data', name='workplace_data'),
    url(r'^activity/$', 'home.data.activity', name='activity'),
    url(r'^details/$', 'home.data.details', name='details'),
    url(r'^send/$', 'home.email.send', name='send'),
    url(r'^send_mail/$', 'home.email.send_mail', name='send_mail'),
    url(r'^send_html/$', 'home.email.send_html', name='send_html'),
    url(r'^send_new_wp/$', 'home.email.send_new_wp', name='send_new_wp'),

    url(r'^change_wp_u/$', 'home.data.change_wp_u', name='change_wp_u'),
    url(r'^change_p_o/$', 'home.data.change_p_o', name='change_p_o'),

    url(r'^products/(?P<id>[^/]+)/edit_desc/$', 'products.views.int_edit_desc', name='int_edit_desc'),
    url(r'^products/(?P<id>[^/]+)/edit_category/$', 'products.views.int_edit_category', name='int_edit_category'),
    url(r'^(?P<id>[^/]+)/set_details/$', 'products.views.set_int_details', name='set_int_details'),
    url(r'^products/(?P<id>[^/]+)/change_image/$', 'products.views.int_change_image', name='int_change_image'),
    url(r'^products/(?P<slug>[^/]+)/$', 'products.views.int_product', name='int_product'),
    url(r'^add_product/$', 'products.views.int_add_product', name='int_add_product'),
    url(r'^category/(?P<slug>[^/]+)/$', 'products.views.int_category', name='int_category'),

)