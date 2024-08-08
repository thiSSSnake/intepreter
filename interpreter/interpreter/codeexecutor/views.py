import uuid
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import json


@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code')
            if not code:
                return JsonResponse({'error': 'No code provided'}, status=400)

            # Unique name of container
            container_name = f"python_interpreter_{uuid.uuid4()}"

            # Launching a container with code transfer via stdin
            result = subprocess.run(
                ['docker', 'run', '--rm','--name', container_name, '-i', '--memory=500m', '--cpus=2', 'python-interpreter', 'python3', '-'],
                input=code.encode('utf-8'),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=30
            )

            output = result.stdout.decode('utf-8')
            error = result.stderr.decode('utf-8')

        except subprocess.TimeoutExpired:
            return JsonResponse({"error": "Execution time out"}, status=500)
        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': f'Execution failed: {e.stderr.decode("utf-8")}'}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        return JsonResponse({'output': output, 'error': error})
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def index(request):
    return render(request, 'index.html', {'csrf_token': request.COOKIES['csrftoken']})
