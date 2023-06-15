module G0 : ASTD_plugin_interfaces.Guard_interface = 
struct 
let [@ocaml.warning "-26"] execute_guard (env_acc : ASTD_environment.environment_accessor) : bool = 
  let first = env_acc#get_string "first" in 
  let eventType = env_acc#get_string "eventType" in 
  let count = env_acc#get_int "count" in 
  let thres = env_acc#get_int "thres" in 
    first = "C:/Windows/System32/tree.com"
end 
let () = ASTD_plugin_builder.register_guard 0 (module G0) 

module G1 : ASTD_plugin_interfaces.Guard_interface = 
struct 
let [@ocaml.warning "-26"] execute_guard (env_acc : ASTD_environment.environment_accessor) : bool = 
  let second = env_acc#get_string "second" in 
  let eventType = env_acc#get_string "eventType" in 
  let count = env_acc#get_int "count" in 
  let thres = env_acc#get_int "thres" in 
    second = "tree  /F"
end 
let () = ASTD_plugin_builder.register_guard 1 (module G1) 

