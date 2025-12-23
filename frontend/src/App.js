import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [todos, setTodos] = useState([])
  const [title, setTitle] = useState('')

  // Fetch todos when component loads
  useEffect(() => {
    fetch('http://localhost:8001/todos/')
      .then(res => res.json())
      .then(data => setTodos(data))
      .catch(err => console.error('Error fetching todos:', err))
  }, [])

  // Add new todo
  const addTodo = () => {
    fetch('http://localhost:8001/todos/?title=' + title, {
      method: 'POST'
    })
      .then(res => res.json())
      .then(newTodo => {
        setTodos([...todos, newTodo])
        setTitle('')
      })
      .catch(err => console.error('Error adding todo:', err))
  }

  // Delete todo
  const deleteTodo = (id) => {
    fetch(`http://localhost:8001/todos/${id}`, {
      method: 'DELETE'
    })
      .then(() => {
        setTodos(todos.filter(todo => todo.id !== id))
      })
      .catch(err => console.error('Error deleting todo:', err))
  }

  return (
    <div className="App">
      <h1>My TODO App</h1>

      <div className="input-section">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter a todo..."
          onKeyPress={(e) => e.key === 'Enter' && addTodo()}
        />
        <button onClick={addTodo}>Add Todo</button>
      </div>

      <ul className="todo-list">
        {todos.map(todo => (
          <li key={todo.id}>
            <span>{todo.title}</span>
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App