<h1>GitHub Webhook Receiver & Activity Viewer</h1>

<p>This project receives GitHub webhook events (push, pull request, and merge) using a Flask backend, stores them in MongoDB Atlas, and displays the events on a live frontend that refreshes every 15 seconds.</p>

<h2> Features</h2>
<ul>
  <li> GitHub webhook integration</li>
  <li> Stores data in MongoDB Atlas</li>
  <li> Frontend to view events live</li>
  <li> Flask backend + HTML/JS frontend</li>
</ul>

<h2> Tech Stack</h2>
<ul>
  <li>Python (Flask)</li>
  <li>MongoDB Atlas (cloud database)</li>
  <li>HTML + JavaScript (Frontend)</li>
  <li>Ngrok (for webhook tunneling)</li>
</ul>

<h2> Setup & Run Locally</h2>

<h3>1. Clone the repo</h3>
<pre><code>git clone https://github.com/your-username/webhook-repo.git
cd webhook-repo</code></pre>

<h3>2. Set up environment</h3>
<pre><code>python -m venv venv
venv\
