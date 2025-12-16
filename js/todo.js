/**
 * Todo List Application with LocalStorage Persistence
 * Fix for INC-001: Completed todos reappear after refresh
 */

const STORAGE_KEY = 'todo_list_items';

// Initialize todos from localStorage or empty array
let todos = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];

/**
 * Save todos to localStorage
 */
function saveTodos() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
}

/**
 * Add a new todo item
 * @param {string} text - The todo text
 */
function addTodo(text) {
    if (!text || text.trim() === '') return;
    
    const todo = {
        id: Date.now(),
        text: text.trim(),
        completed: false,
        createdAt: new Date().toISOString()
    };
    
    todos.push(todo);
    saveTodos();
    renderTodos();
}

/**
 * Toggle todo completion status
 * @param {number} id - The todo id
 */
function toggleTodo(id) {
    const todo = todos.find(t => t.id === id);
    if (todo) {
        todo.completed = !todo.completed;
        todo.updatedAt = new Date().toISOString();
        saveTodos(); // Persist the completion state to localStorage
        renderTodos();
    }
}

/**
 * Delete a todo item
 * @param {number} id - The todo id
 */
function deleteTodo(id) {
    todos = todos.filter(t => t.id !== id);
    saveTodos();
    renderTodos();
}

/**
 * Render all todos to the DOM
 */
function renderTodos() {
    const todoList = document.getElementById('todo-list');
    if (!todoList) return;
    
    todoList.innerHTML = '';
    
    todos.forEach(todo => {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
        li.dataset.id = todo.id;
        
        li.innerHTML = `
            <input type="checkbox" 
                   class="todo-checkbox" 
                   ${todo.completed ? 'checked' : ''} 
                   onchange="toggleTodo(${todo.id})">
            <span class="todo-text">${escapeHtml(todo.text)}</span>
            <button class="delete-btn" onclick="deleteTodo(${todo.id})">Delete</button>
        `;
        
        todoList.appendChild(li);
    });
}

/**
 * Escape HTML to prevent XSS
 * @param {string} text - Text to escape
 * @returns {string} Escaped text
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Handle form submission
 * @param {Event} event - Form submit event
 */
function handleSubmit(event) {
    event.preventDefault();
    const input = document.getElementById('todo-input');
    if (input) {
        addTodo(input.value);
        input.value = '';
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Load and render todos from localStorage
    renderTodos();
    
    // Set up form handler
    const form = document.getElementById('todo-form');
    if (form) {
        form.addEventListener('submit', handleSubmit);
    }
});
