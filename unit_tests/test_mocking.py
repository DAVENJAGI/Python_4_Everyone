def monthly_schedule(self, month):
    response = request.get(f'http://company.com/{self.name}/ {month}')
    if response.ok:
        return response.text
    else:
        return 'Bad Response!'
