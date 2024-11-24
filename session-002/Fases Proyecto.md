# Fases del proyecto

De lo que vimos de la lluvia de ideas.

# Fase 1
- Registro de usuario e ingreso a la plataforma.
	- Un formulario de registro.
		- El usuario registra datos.
		- El registro de usuario queda guardado  en el sistema.
			- Frontend: la vista del formulario sus validaciones.
			- Backend: servicio de creación de usuario.
			- El perfil requiera una aprobación de la empresa. (queda como 
			  stand-by hasta que me dan la aprobación)
	- Backoffice
		- Lista de usuarios.
		- Paginado.
		- Buscar por nombre o email.
		- Aprobar o no aprobar registro (crear el proyecto, base de código, 
		  repos, etc...)

# Fase 2
- Login de usuario y entrada al dashboard
- Dashboard:
	- contenido dummy (planificamos qué va a ir, por ejemplo saldo, últimas 
	  compras, etc.)
	- Perfil de usuario, cambiar password.
- Backoffice
	- Reiniciar la contraseña de un usuario. 

# Fase 3
- Funcionalidad de cargar saldo en Tokens
	- Formulario compra.
		- Elegir monto.
		- Medio de pago (Tarjeta o pagar en efectivo en Oxxo) Caso tarjeta 
		  llenar datos y pagar
		- Costo de token: Hacemos un API que simule el costo del token.
		- Pago con tarjeta: Hacemos un API que simule una transacción con la 
		  tarjeta .
	- Agrego que el dashboard cargue la data real de la BD.
- Backoffice
	- Reporte de transacciones.
		- Buscar por rango de fecha.
		- Buscar por usuario.
		- Generar un excel o pdf con el reporte.

# Fase 4
- 2FA de autenticación. 
	- Servicio de email o Whatsapp o SMS con capa gratis para probar el envío 
	  de un token.
	- Google Auth (capa gratis)