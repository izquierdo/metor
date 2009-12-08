var map;
var chart = null;
var estaciones = [
    {
        name: "Jose",
        lat: 10.083,
        lng: -64.917,
        altura: 100,
        rosa: "resources/images/rosa.png",
        temperatura: [26.19,13.98,27.69,29.93,26.66,23.13,19.86,31.57,29.49,28.69,21.63,18.67,19.30,28.40,24.98,24.36,19.75,26.59,29.42,14.97,25.01,19.27,26.28,35.28,32.21,28.88,29.29,29.95,25.62,23.97,31.60,19.83,31.94,20.43,25.53,23.62,28.25,21.48,18.01,23.93,32.66,22.89,23.60,21.03,33.81,13.39,14.85,22.07,26.01,28.87,17.98,17.08,22.66,31.79,24.67,31.08,24.27,18.58,30.95,26.28],
        presion: [4.83,5.37,5.33,5.25,4.61,4.86,4.76,4.98,4.00,5.03,4.80,5.12,4.86,5.32,5.65,5.28,5.82,4.59,5.52,5.81,4.29,4.63,4.52,4.57,5.03,4.97,5.21,5.11,5.60,6.21,4.96,4.72,4.94,4.55,4.71,4.98,5.55,4.56,5.49,4.83,4.84,4.85,5.13,5.00,5.13,5.22,4.34,4.23,3.74,5.08,4.41,4.78,4.78,5.27,5.38,5.63,4.00,5.11,5.67,4.11],
        fecha: [[2009, 9, 1], [2009, 9, 2], [2009, 9, 3], [2009, 9, 4], [2009, 9, 5], [2009, 9, 6], [2009, 9, 7], [2009, 9, 8], [2009, 9, 9], [2009, 9, 10], [2009, 9, 11], [2009, 9, 12], [2009, 9, 13], [2009, 9, 14], [2009, 9, 15], [2009, 9, 16], [2009, 9, 17], [2009, 9, 18], [2009, 9, 19], [2009, 9, 20], [2009, 9, 21], [2009, 9, 22], [2009, 9, 23], [2009, 9, 24], [2009, 9, 25], [2009, 9, 26], [2009, 9, 27], [2009, 9, 28], [2009, 9, 29], [2009, 9, 30], [2009, 9, 31], [2009, 10, 1], [2009, 10, 2], [2009, 10, 3], [2009, 10, 4], [2009, 10, 5], [2009, 10, 6], [2009, 10, 7], [2009, 10, 8], [2009, 10, 9], [2009, 10, 10], [2009, 10, 11], [2009, 10, 12], [2009, 10, 13], [2009, 10, 14], [2009, 10, 15], [2009, 10, 16], [2009, 10, 17], [2009, 10, 18], [2009, 10, 19], [2009, 10, 20], [2009, 10, 21], [2009, 10, 22], [2009, 10, 23], [2009, 10, 24], [2009, 10, 25], [2009, 10, 26], [2009, 10, 27], [2009, 10, 28], [2009, 10, 29]]
    },
    {
        name:"Barcelona",
        lat: 10.133,
        lng: -64.7,
        altura: 25,
        rosa: "resources/images/rosa3.png",
        temperatura: [20.64,16.53,21.15,17.02,20.44,25.17,23.89,20.82,24.26,23.75,19.10,21.80,17.47,20.90,25.43,20.91,19.47,26.44,19.52,21.41,24.23,21.96,22.20,19.45,20.26,24.36,26.03,22.82,20.73,22.48,24.77,21.86,18.34,21.61,25.70,19.16,27.85,29.57,25.11,21.52,26.52,21.24,20.88,19.93,23.72,18.30,25.74,22.17,20.10,26.32,23.62,25.95,22.54,22.09,23.88,20.15,22.26,19.36,18.75,22.46],
        presion: [6.30,6.44,7.83,9.20,7.44,8.63,10.14,7.76,10.55,9.81,10.10,7.70,9.25,7.26,9.66,9.15,8.72,9.47,9.14,9.31,9.20,8.31,9.96,9.13,9.82,8.43,7.26,10.21,8.21,8.76,9.76,9.02,8.89,8.47,7.90,8.59,6.95,8.39,7.36,10.34,9.78,10.41,9.19,9.64,8.58,8.43,8.75,7.40,7.65,8.68,8.36,9.36,10.02,9.05,8.69,7.82,7.73,10.17,9.57,8.56],
        fecha: [[2009, 9, 1], [2009, 9, 2], [2009, 9, 3], [2009, 9, 4], [2009, 9, 5], [2009, 9, 6], [2009, 9, 7], [2009, 9, 8], [2009, 9, 9], [2009, 9, 10], [2009, 9, 11], [2009, 9, 12], [2009, 9, 13], [2009, 9, 14], [2009, 9, 15], [2009, 9, 16], [2009, 9, 17], [2009, 9, 18], [2009, 9, 19], [2009, 9, 20], [2009, 9, 21], [2009, 9, 22], [2009, 9, 23], [2009, 9, 24], [2009, 9, 25], [2009, 9, 26], [2009, 9, 27], [2009, 9, 28], [2009, 9, 29], [2009, 9, 30], [2009, 9, 31], [2009, 10, 1], [2009, 10, 2], [2009, 10, 3], [2009, 10, 4], [2009, 10, 5], [2009, 10, 6], [2009, 10, 7], [2009, 10, 8], [2009, 10, 9], [2009, 10, 10], [2009, 10, 11], [2009, 10, 12], [2009, 10, 13], [2009, 10, 14], [2009, 10, 15], [2009, 10, 16], [2009, 10, 17], [2009, 10, 18], [2009, 10, 19], [2009, 10, 20], [2009, 10, 21], [2009, 10, 22], [2009, 10, 23], [2009, 10, 24], [2009, 10, 25], [2009, 10, 26], [2009, 10, 27], [2009, 10, 28], [2009, 10, 29]]
    },
    {
        name: "Puerto Píritu",
        lat: 10.06667,
        lng: -65.05,
        altura: 40,
        rosa: "resources/images/rosa4.png",
        temperatura: [30.37,34.67,30.34,29.88,41.17,16.23,23.53,12.09,15.75,19.24,13.40,17.73,27.49,19.04,20.06,10.46,24.15,9.31,25.52,17.13,0.97,19.18,19.75,15.93,15.88,27.22,12.35,19.90,28.11,17.16,24.78,26.62,18.74,25.64,24.32,24.13,22.86,17.52,28.89,35.06,19.79,13.22,14.78,26.36,24.16,19.96,17.86,8.51,23.76,25.21,14.31,21.21,27.59,21.03,32.70,18.98,25.80,28.01,20.24,17.87],
        presion: [1.76,0.47,1.48,5.65,4.96,3.14,-1.70,2.10,3.10,3.33,1.96,2.07,5.60,5.60,-0.12,2.29,2.43,1.18,1.52,2.58,3.72,3.55,4.81,0.63,1.02,3.41,2.83,2.32,4.47,0.56,1.35,6.10,3.23,-0.40,3.77,5.91,0.10,3.80,4.85,2.27,2.31,0.54,4.98,5.55,1.85,4.51,5.74,3.16,4.16,2.33,3.39,-0.00,5.22,-0.89,0.77,2.58,1.61,2.25,5.01,3.88],
        fecha: [[2009, 9, 1], [2009, 9, 2], [2009, 9, 3], [2009, 9, 4], [2009, 9, 5], [2009, 9, 6], [2009, 9, 7], [2009, 9, 8], [2009, 9, 9], [2009, 9, 10], [2009, 9, 11], [2009, 9, 12], [2009, 9, 13], [2009, 9, 14], [2009, 9, 15], [2009, 9, 16], [2009, 9, 17], [2009, 9, 18], [2009, 9, 19], [2009, 9, 20], [2009, 9, 21], [2009, 9, 22], [2009, 9, 23], [2009, 9, 24], [2009, 9, 25], [2009, 9, 26], [2009, 9, 27], [2009, 9, 28], [2009, 9, 29], [2009, 9, 30], [2009, 9, 31], [2009, 10, 1], [2009, 10, 2], [2009, 10, 3], [2009, 10, 4], [2009, 10, 5], [2009, 10, 6], [2009, 10, 7], [2009, 10, 8], [2009, 10, 9], [2009, 10, 10], [2009, 10, 11], [2009, 10, 12], [2009, 10, 13], [2009, 10, 14], [2009, 10, 15], [2009, 10, 16], [2009, 10, 17], [2009, 10, 18], [2009, 10, 19], [2009, 10, 20], [2009, 10, 21], [2009, 10, 22], [2009, 10, 23], [2009, 10, 24], [2009, 10, 25], [2009, 10, 26], [2009, 10, 27], [2009, 10, 28], [2009, 10, 29]]
    },
    {
        name: "El Tigre",
        lat: 9.91667,
        lng: -65.08333,
        altura: 520,
        rosa: "resources/images/rosa5.png",
        temperatura: [6.21,44.92,37.96,19.17,17.84,24.73,24.63,16.74,30.97,26.29,21.62,29.32,30.55,31.59,27.28,13.85,38.24,16.02,21.56,14.10,24.12,39.09,39.99,35.97,19.66,36.10,12.69,22.86,40.70,31.18,32.71,23.24,6.64,34.62,28.67,32.57,38.75,35.14,27.84,31.81,28.31,28.29,21.19,37.40,27.64,32.94,31.76,38.76,31.26,29.76,26.51,29.64,36.31,42.16,20.73,33.23,33.12,35.25,35.32,25.97],
        presion: [-8.57,-5.58,-3.99,0.12,-1.92,6.39,3.99,5.78,0.78,1.06,7.01,10.85,9.04,7.02,-3.76,2.49,0.53,3.59,-3.10,4.98,6.73,0.19,2.47,3.14,-2.74,2.92,-1.07,2.12,-3.90,7.71,-2.35,0.27,-0.34,3.88,-3.85,-0.91,4.51,-4.41,7.84,3.09,8.87,2.05,-2.48,-2.23,-0.84,6.29,2.04,-1.21,6.80,1.73,7.90,-5.28,4.11,6.19,2.86,8.12,7.51,-3.14,2.88,7.85],
        fecha: [[2009, 9, 1], [2009, 9, 2], [2009, 9, 3], [2009, 9, 4], [2009, 9, 5], [2009, 9, 6], [2009, 9, 7], [2009, 9, 8], [2009, 9, 9], [2009, 9, 10], [2009, 9, 11], [2009, 9, 12], [2009, 9, 13], [2009, 9, 14], [2009, 9, 15], [2009, 9, 16], [2009, 9, 17], [2009, 9, 18], [2009, 9, 19], [2009, 9, 20], [2009, 9, 21], [2009, 9, 22], [2009, 9, 23], [2009, 9, 24], [2009, 9, 25], [2009, 9, 26], [2009, 9, 27], [2009, 9, 28], [2009, 9, 29], [2009, 9, 30], [2009, 9, 31], [2009, 10, 1], [2009, 10, 2], [2009, 10, 3], [2009, 10, 4], [2009, 10, 5], [2009, 10, 6], [2009, 10, 7], [2009, 10, 8], [2009, 10, 9], [2009, 10, 10], [2009, 10, 11], [2009, 10, 12], [2009, 10, 13], [2009, 10, 14], [2009, 10, 15], [2009, 10, 16], [2009, 10, 17], [2009, 10, 18], [2009, 10, 19], [2009, 10, 20], [2009, 10, 21], [2009, 10, 22], [2009, 10, 23], [2009, 10, 24], [2009, 10, 25], [2009, 10, 26], [2009, 10, 27], [2009, 10, 28], [2009, 10, 29]]
    }
];


function mostrarEstacion(i, estacion){
    $('#datosestacion').show();
    $('#estacionid').html(estacion.name);
    $('#list').attr('selectedIndex', i);
    $('#info')
        .empty()
        .append($('<li />').html('Coordenadas: '+estacion.lat + ", " + estacion.lng))
        .append($('<li />').html('Altura: '+estacion.altura+' msndm'));
        //.append($('<li />').html('Último valor: 2009-10-11 12:32:00'))

    $('#rosa').attr('src', estacion.rosa);
    var latlng = new GLatLng(estacion.lat, estacion.lng);
    map.openInfoWindowHtml(latlng, '<b>'+estacion.name+'</b><br/><small>' +
                           estacion.lat + ", " + estacion.lng+"</small>");


    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Date');
    data.addColumn('number', 'Temperatura');
    data.addColumn('number', 'Presión');

    var rows = [];
    for(var i=0; i<estacion.temperatura.length; ++i){
        rows[i] = [new Date(estacion.fecha[i][0], estacion.fecha[i][1], estacion.fecha[i][2]),
                   estacion.temperatura[i],
                   estacion.presion[i]
                  ];
    }
    data.addRows(rows);

    if (chart == null){
        chart = new google.visualization.AnnotatedTimeLine(document.getElementById('chart_div'));
    }
    chart.draw(data, {displayAnnotations: false, allowRedraw: true});
    
}

$(document).ready(function(){
    if (GBrowserIsCompatible()) {
        map = new GMap2(document.getElementById("map"));
        map.setCenter(new GLatLng(10.083,-64.917), 10);
        map.setMapType(G_PHYSICAL_MAP);
        var markers = {};
        $(estaciones).each(function(i, val){
            var latlng = new GLatLng(val.lat, val.lng);
            var marker = new GMarker(latlng);
            map.addOverlay(marker);
            markers[val[0]] = marker;

            var activate = function(){
                mostrarEstacion(i, val);
                //
                // map.panTo(marker.getLatLng());
            };

            GEvent.addListener(marker, "click", activate);
            $("<li />")
                .html(val.name)
                .click(activate)
                .appendTo("#list");
        });

        map.setUIToDefault();
    }
});        
