Rails.application.routes.draw do
  resources :messages
  root 'messages#new'
end
