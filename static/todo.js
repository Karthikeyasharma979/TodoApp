document.addEventListener('DOMContentLoaded', () => {
    const todoForm = document.getElementById('todo-form');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');
    const filterStatus = document.getElementById('filter-status');
    const logoutBtn = document.getElementById('logout-btn');

    // Load todos from localStorage
    let todos = JSON.parse(localStorage.getItem('todos')) || [];

    function saveTodos() {
        localStorage.setItem('todos', JSON.stringify(todos));
    }

    function renderTodos() {
        const filter = filterStatus.value;
        const filteredTodos = todos.filter(todo => {
            if (filter === 'active') return !todo.completed;
            if (filter === 'completed') return todo.completed;
            return true;
        });

        todoList.innerHTML = '';
        
        filteredTodos.forEach((todo, index) => {
            const li = document.createElement('li');
            li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
            
            li.innerHTML = `
                <input type="checkbox" class="form-check-input" 
                    ${todo.completed ? 'checked' : ''}>
                <span class="todo-text">${todo.text}</span>
                <div class="todo-actions">
                    <button class="btn btn-sm btn-danger">Delete</button>
                </div>
            `;

            const checkbox = li.querySelector('input[type="checkbox"]');
            checkbox.addEventListener('change', () => toggleTodo(index));

            const deleteBtn = li.querySelector('.btn-danger');
            deleteBtn.addEventListener('click', () => deleteTodo(index));

            todoList.appendChild(li);
        });
    }

    function addTodo(text) {
        todos.push({ text, completed: false });
        saveTodos();
        renderTodos();
    }

    function toggleTodo(index) {
        todos[index].completed = !todos[index].completed;
        saveTodos();
        renderTodos();
    }

    function deleteTodo(index) {
        todos.splice(index, 1);
        saveTodos();
        renderTodos();
    }

    function handleLogout() {
        // Clear todos from localStorage
        localStorage.removeItem('todos');
        // Reset todos array
        todos = [];
        // Re-render the empty list
        renderTodos();
        // Optional: Show feedback
        alert('Successfully logged out!');
    }

    todoForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const text = todoInput.value.trim();
        if (text) {
            addTodo(text);
            todoInput.value = '';
        }
    });

    filterStatus.addEventListener('change', renderTodos);
    logoutBtn.addEventListener('click', handleLogout);

    // Initial render
    renderTodos();
});