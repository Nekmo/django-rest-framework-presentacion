Presentación
============
Buenas, soy Juan José Oyague, más conocido en las redes como Nekmo; y llevo media vida programando en Python, usando
Django ya desde su versión 1.1. Así que no os puedo engañar...

... me gusta Django, y Django Rest Framework (diapositiva corazón). Pero espero poder conseguir haceros llegar un poco
de mi pasión por estos dos frameworks, y de los motivos por los que llevo usándolos tanto tiempo.

Vale, pero antes de Django Rest Framework, llegó Django. ¿Qué es exactamente? Aquí no me puedo parar mucho, pero en
resumen, Django es un framework web para el rápido desarrollo en Python, con miles de módulos, muy estable y con gran
soporte. Seguramente, el más conocido y usado en Python.

Y al igual que Python, tiene baterías incluidas para todo. ORM para base de datos, administración de sesiones,
control de permisos, gestión de urls, middleware, caché, envío de correos... Pero claro, no API Rest.

Django Rest framework (diapositiva). ¿Recordáis que hemos dicho que tiene módulos para todo? Pues Django
Rest Framework es uno de esos módulos. Se instala en prácticamente en 3 o 4 pasos y listo para funcionar.

Pero espera... Django Rest Framework es un framework... ¿Y Django también es un framework? - (diapositiva meme meta).

Sí, Django Rest Framework es un framework dentro de otro framework web. Pero aún no saquéis las antorchas (diapositiva
antorchas Simpsons).

Django Rest Framework aprovecha todo lo bueno de Django, y lo complementa. Si Django es un pastel (diapositiva pastel -
Django Rest Framework) es su guinda (diapositiva pastel con guida). ¿Y nadie quiere una guinda sin pastel, verdad?


Vale, empecemos por los serializers. ¿Y qué hacen los serializers? -- "Los serializers, serializan -- J. Oyague, 2021"
(diapositiva). Vale, ya enserio.

Los serializers, son los responsables de convertir la entrada de datos, vamos, lo que mete el usuario a través de la
API, en un objeto en Python, que normalmente servirá para crear o actualizar un objeto en la base de datos. También
hacen lo mismo pero a la inversa: convierten el objeto a una salida compatible, para que nos entendamos, un
diccionario, y devolverlo al usuario.

(código de ejemplo de serializer)

Los viewsets en cambio, son la lógica encargada de devolver tus objetos, a través de la API, crearlos, listarlos, etc.
Por ejemplo, el viewset ``UserViewSet`` tendrá las siguientes acciones para trabajar con los usuarios: listar, crear,
obtener y eliminar (ejemplo código: https://www.django-rest-framework.org/api-guide/viewsets/ ).

El viewset no sólo se encarga de esto: también define los llamados *parsers* que son las formas de leer la información
del usuario para aceptar json, xml, entre otros, y los *renders*, para devolver los datos según pueda quererlo el
usuario.

No sólo esto, sino que se encargan de muchas cosas más, como *filtrado y paginación en los listados paginación*,
*permisos y autenticación*, *caché*, *documentación* y mucho más.

Vale, y hasta aquí la mitad de la presentación. (diapositiva de aplausos) Lo que queda por suerte ya es más fácil.

Los *routers* son la parte más sencilla de explicar: se encargan de registrar los viewsets y ponerles un nombre, para
que sea posible acceder a ellos por una url. ¿No es genial acabar con la parte más fácil? - Después sólo queda
registrarlos en el ``urls.py`` de Django, igual que con cualquier otra app. Así de fácil.

Así pues, en resumen tenemos: serializers que representan e interpretan los datos, viewsets que gestionan las
peticiones, y routers que corresponde a las urls que se utilizarán.

Pero claro, alguno pensará... ¡Esas son muchas clases y muchas cosas! ¿No podría estar todo junto? A mí también me ha
pasado al principio. Por ejemplo, ¿por qué no juntar los serializers y los viewsets? El motivo, es que puedes heredar
de tu serializer para crear uno en mas detalle (ejemplo de código) - Y devolver un serializer u otro dependiendo de si
lo pones en un listado o pides sólo uno, por ejemplo (ejemplo de código). Así ahorras datos. ¿No es genial? Y por si
fuera poco, puedes reutilizar tus serializers para usarlos en otros serializers, anidados (ejemplo código). Esto es
lo que se llama *nested serializers*. La gente de Django Rest Framework ha pensado en muchas de estas cosas, pero si
fuera poco, cuentas con cientos de módulos de terceros, como por ejemplo (listar ejemplos).

Aunque hay módulos para swagger, documentación adicional y más, Django Rest Framework ya incluye una interfaz
navegable muy avanzada y fácil de usar. Vamos a ver un ejemplo con, por ejemplo, - diapositiva pikachu - pokémon.
Porque, ¿por qué no?

(presentación versión web Django Rest Framework)

Y hasta aquí la presentación. Espero que no se haya alargado de más. Tenéis enlaces a Django, Django Rest Framework y
a mi sitio web (ejem ejem spam) en esta diapositiva. Y también mi email. Y Twitter. Aunque apenas escriba en Twitter.
Y ante todo, ¡muchas gracias a todos!
