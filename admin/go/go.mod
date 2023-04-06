module github.com/onlineconf/onlineconf/admin/go

go 1.13

require (
	github.com/bmatcuk/doublestar/v4 v4.4.0
	github.com/go-sql-driver/mysql v1.6.0
	github.com/gorilla/handlers v1.4.2
	github.com/gorilla/mux v1.7.3
	github.com/rs/zerolog v1.15.0
	github.com/ugorji/go/codec v1.1.7
	github.com/ugorji/go/codec/codecgen v1.1.7
	gitlab.com/nyarla/go-crypt v0.0.0-20160106005555-d9a5dc2b789b
	gopkg.in/yaml.v3 v3.0.1
)

replace github.com/bmatcuk/doublestar/v4 v4.4.0 => github.com/AndrewDeryabin/doublestar/v4 v4.0.0-20230123130924-38953b2ce9a0
