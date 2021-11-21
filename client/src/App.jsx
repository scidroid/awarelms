import { useAuth0 } from "@auth0/auth0-react"
import useFetch from "react-fetch-hook"

const addMsg = (name, description) => {
  msg = JSON.stringify({
    name: name,
    description: description
  })
  const URL = "https://lopsidedsophisticateddeveloper.scidroid.repl.co/ms";
  fetch(URL, {
  method: 'POST',
  body: msg,
  headers:{
    'Content-Type': 'application/json'
  }
}).then(res => res.json())
.catch(error => console.error('Error:', error))
.then(response => console.log('Success:', response));
};

const App = () => {
  const { loginWithRedirect, isAuthenticated } = useAuth0();
  const {data} = useFetch("https://lopsidedsophisticateddeveloper.scidroid.repl.co/ms");
  const ms = data._items;
  if (!isAuthenticated) {
    loginWithRedirect()
  }
  return (
    <div>
    {ms.map((m, k) => (
      <div key={k}>
      <h2>{m.name}</h2>
      <p>{m.description}</p>
      </div>
    ))}
    </div>
  )
}

export default App;
