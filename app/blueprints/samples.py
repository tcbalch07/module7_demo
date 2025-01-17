from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

samples = Blueprint('samples', __name__)

@samples.route('/sample', methods=['GET', 'POST'])
def sample():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new runner
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        # Insert the new runner into the database
        cursor.execute('INSERT INTO samples (sample_name, sample_size) VALUES (%s, %s)', (first_name, last_name))
        db.commit()

        flash('New sample added successfully!', 'success')
        return redirect(url_for('samples.sample'))

    # Handle GET request to display all runners
    cursor.execute('SELECT * FROM samples')
    all_runners = cursor.fetchall()
    return render_template('samples.html', all_samples=all_samples)

@samples.route('/update_sample/<int:sample_id>', methods=['GET', 'POST'])
def update_sample(sample_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the runner's details
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        cursor.execute('UPDATE samples SET sample_name = %s, sample_size = %s WHERE sample_id = %s', (sample_name, sample_size, sample_id))
        db.commit()

        flash('Sample updated successfully!', 'success')
        return redirect(url_for('samples.sample'))

    # GET method: fetch runner's current data for pre-populating the form
    cursor.execute('SELECT * FROM samples WHERE sample_id = %s', (sample_id,))
    current_runner = cursor.fetchone()
    return render_template('update_sample.html', current_sample=current_sample)

@samples.route('/delete_sample/<int:sample_id>', methods=['POST'])
def delete_sample(sample_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the runner
    cursor.execute('DELETE FROM samples WHERE sample_id = %s', (sample_id,))
    db.commit()

    flash('Sample deleted successfully!', 'danger')
    return redirect(url_for('samples.sample'))