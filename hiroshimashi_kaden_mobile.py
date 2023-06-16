import folium

m = folium.Map(location=[34.45,132.4],zoom_start=11)
m

folium.Marker(location=[34.3968748,132.4985497],popup='エディオン 安芸府中店　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.3720978,132.3962754],popup='エディオン アルパーク南店　　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.3716024,132.35532],popup='エディオン 五日市店　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.3640794,132.4580432],popup='エディオン 宇品店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.5204077,132.4998783],popup='エディオン 可部店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.4724838,132.5140842],popup='エディオン 高陽店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.3957049,132.4768341],popup='エディオン 蔦屋家電　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.468192,132.4191645],popup='エディオン 沼田店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.3952982,132.4560839],popup='エディオン 広島本店 西館　　　　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.4778007,132.4922729],popup='エディオン 八木店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.3616664,132.3520525],popup='ヤマダデンキ テックランド佐伯店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.478507,132.492709],popup='ヤマダデンキ テックランド広島八木店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3860355,132.4642703],popup='ヤマダデンキ テックランドフジグラン広島店　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3584712,132.4565332],popup='ヤマダデンキ テックランドゆめタウンみゆき店　　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3739044,132.3958979],popup='ヤマダデンキ ヤマダアウトレット&ホビー館 アルパーク前店　　　　　　　　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3931861,132.4637685],popup='ヤマダデンキ LABI広島店　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3724299,132.3931736],popup='ヤマダデンキ Tecc LIFE SELECT 広島アルパーク店　　　　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.3946637,132.4993689],popup='コジマ×ビックカメラ イオンモール広島府中店　　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="lightred")).add_to(m)
m

folium.Marker(location=[34.363356,132.470272],popup='コジマ×ビックカメラ 宇品店　　　　　　　　　　　　',icon=folium.Icon(color="lightred")).add_to(m)
m

folium.Marker(location=[34.466147,132.4776],popup='コジマ×ビックカメラ 広島インター緑井店　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="lightred")).add_to(m)
m

folium.Marker(location=[34.3957633,132.4749874],popup='ビックカメラ 広島駅前店　　　　　　　　　　　',icon=folium.Icon(color="lightred")).add_to(m)
m

folium.Marker(location=[34.3920098,132.4785077],popup='ケーズデンキ 広島本店　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[34.4427442,132.4611678],popup='イオンモバイル 広島祇園店　　　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[34.3953374,132.4986208],popup='イオンモバイル 広島府中店　　　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[34.3975903,132.4735216],popup='マーキュリー 中四国支店　　　　　　　　　　　',icon=folium.Icon(color="white")).add_to(m)
m

m.save('hiroshimashi_kaden_mobile.html')
